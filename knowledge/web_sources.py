#!/usr/bin/env python3
"""Search public web pages and import only a user-selected result."""

from __future__ import annotations

import hashlib
import html
import ipaddress
import importlib.util
import json
import re
import socket
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


PROJECT_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_ROOT = PROJECT_ROOT / "knowledge"
DEFAULT_INBOX = KNOWLEDGE_ROOT / "inbox"
DEFAULT_RAW = KNOWLEDGE_ROOT / "raw"
DEFAULT_SEARCH_RESULTS = PROJECT_ROOT / "runs" / "day17-web-search.json"
SEARCH_ENDPOINT = "https://lite.duckduckgo.com/lite/"
MAX_QUERY_LENGTH = 300
MAX_RESULTS = 5
MAX_SEARCH_BYTES = 2 * 1024 * 1024
MAX_SOURCE_BYTES = 20 * 1024 * 1024
USER_AGENT = "LocalEngineeringKnowledgeAssistant/0.1 (Day17 web search)"

_SCRIPTS = PROJECT_ROOT / "skills" / "source-to-raw-md" / "scripts"
_BATCH_MODULE = None


class WebSearchError(RuntimeError):
    """The search provider or selected source could not be used safely."""


class _SearchResults(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[dict[str, str]] = []
        self._anchor: dict[str, str] | None = None
        self._snippet: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "a" and classes.intersection({"result__a", "result-link"}):
            self._anchor = {"url": values.get("href") or "", "title": ""}
        elif tag in {"div", "a", "td"} and classes.intersection(
            {"result__snippet", "result-snippet"}
        ):
            self._snippet = {"text": ""}

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._anchor is not None:
            self.items.append({**self._anchor, "snippet": ""})
            self._anchor = None
        if tag in {"div", "a", "td"} and self._snippet is not None:
            if self.items and not self.items[-1]["snippet"]:
                self.items[-1]["snippet"] = self._snippet["text"].strip()
            self._snippet = None

    def handle_data(self, data: str) -> None:
        if self._anchor is not None:
            self._anchor["title"] += data
        if self._snippet is not None:
            self._snippet["text"] += data


def _public_http_url(url: str) -> str:
    try:
        parts = urlsplit(url)
        port = parts.port or (443 if parts.scheme == "https" else 80)
    except ValueError as error:
        raise WebSearchError(f"網址格式無效：{url}") from error
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise WebSearchError("只接受完整的 HTTP 或 HTTPS 網址")
    if parts.username or parts.password:
        raise WebSearchError("網址不可包含帳號或密碼")
    hostname = parts.hostname.rstrip(".").lower()
    try:
        addresses = {ipaddress.ip_address(hostname)}
    except ValueError:
        if hostname == "localhost" or hostname.endswith((".localhost", ".local", ".internal")):
            raise WebSearchError("不接受本機或內部網域")
        try:
            addresses = {
                ipaddress.ip_address(item[4][0].split("%", 1)[0])
                for item in socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
            }
        except OSError as error:
            raise WebSearchError(f"無法解析來源網址主機：{hostname}") from error
    if not addresses or any(not address.is_global for address in addresses):
        raise WebSearchError("不接受解析到非公開 IP 位址的網址")
    return url


class _PublicRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, newurl):
        target = urljoin(request.full_url, newurl)
        _public_http_url(target)
        return super().redirect_request(request, response, code, message, headers, target)


def fetch_url(
    url: str,
    *,
    max_bytes: int,
    allowed_types: set[str],
) -> tuple[bytes, str, str, str]:
    """Fetch one public URL and return bytes, final URL, MIME type, and charset."""

    _public_http_url(url)
    opener = build_opener(_PublicRedirectHandler())
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/pdf,text/plain"})
    try:
        with opener.open(request, timeout=20) as response:
            final_url = _public_http_url(response.geturl())
            content_type = response.headers.get_content_type().lower()
            charset = response.headers.get_content_charset() or "utf-8"
            if content_type not in allowed_types:
                raise WebSearchError(f"網頁格式不支援：{content_type}")
            data = response.read(max_bytes + 1)
    except HTTPError as error:
        raise WebSearchError(f"來源伺服器回傳 HTTP {error.code}") from error
    except (URLError, TimeoutError, OSError) as error:
        raise WebSearchError(f"無法讀取網頁：{error}") from error
    if len(data) > max_bytes:
        raise WebSearchError(f"來源超過 {max_bytes} bytes 上限")
    return data, final_url, content_type, charset


def _result_url(href: str) -> str:
    if not href:
        return ""
    absolute = urljoin(SEARCH_ENDPOINT, html.unescape(href))
    parsed = urlsplit(absolute)
    if parsed.hostname and parsed.hostname.endswith("duckduckgo.com") and parsed.path == "/l/":
        redirect = parse_qs(parsed.query).get("uddg", [])
        if redirect:
            return html.unescape(redirect[0])
    return absolute


def parse_search_results(document: str, *, limit: int = MAX_RESULTS) -> list[dict[str, str]]:
    parser = _SearchResults()
    parser.feed(document)
    results: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in parser.items:
        title = re.sub(r"\s+", " ", html.unescape(item["title"])).strip()
        url = _result_url(item["url"])
        snippet = re.sub(r"\s+", " ", html.unescape(item["snippet"])).strip()
        if not title or not url or url in seen:
            continue
        try:
            _public_http_url(url)
        except WebSearchError:
            continue
        seen.add(url)
        results.append({"title": title[:240], "url": url, "snippet": snippet[:500]})
        if len(results) >= limit:
            break
    return results


def _atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    try:
        temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def web_search(
    *,
    query: str,
    results_path: Path = DEFAULT_SEARCH_RESULTS,
    fetcher: Callable[..., tuple[bytes, str, str, str]] = fetch_url,
) -> dict[str, Any]:
    """Search the web and persist a bounded candidate list for a later user choice."""

    if not isinstance(query, str) or not query.strip():
        raise WebSearchError("query 不可為空")
    query = query.strip()
    if len(query) > MAX_QUERY_LENGTH:
        raise WebSearchError(f"query 不可超過 {MAX_QUERY_LENGTH} 個字元")
    saved_at = datetime.now(timezone.utc).isoformat()
    _atomic_json(
        results_path,
        {"version": 1, "query": query, "saved_at": saved_at, "results": []},
    )
    document, _, _, charset = fetcher(
        SEARCH_ENDPOINT + "?" + urlencode({"q": query}),
        max_bytes=MAX_SEARCH_BYTES,
        allowed_types={"text/html"},
    )
    try:
        page = document.decode(charset, errors="replace")
    except LookupError:
        page = document.decode("utf-8", errors="replace")
    if "challenge-submit" in page or "confirm this search was made by a human" in page.lower():
        raise WebSearchError("搜尋服務要求人工驗證，這次沒有取得搜尋結果")
    results = parse_search_results(page)
    candidates = [
        {"source_id": f"web-{index}", **result}
        for index, result in enumerate(results, start=1)
    ]
    state = {
        "version": 1,
        "query": query,
        "saved_at": saved_at,
        "results": candidates,
    }
    _atomic_json(results_path, state)
    return {"query": query, "result_count": len(candidates), "results": candidates}


def _read_candidates(results_path: Path) -> dict[str, dict[str, str]]:
    try:
        state = json.loads(results_path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise WebSearchError("目前沒有可匯入的搜尋結果；請先呼叫 web_search") from error
    except (OSError, json.JSONDecodeError) as error:
        raise WebSearchError(f"搜尋結果紀錄無法讀取：{error}") from error
    if not isinstance(state, dict) or state.get("version") != 1 or not isinstance(state.get("results"), list):
        raise WebSearchError("搜尋結果紀錄格式錯誤")
    candidates: dict[str, dict[str, str]] = {}
    for item in state["results"]:
        if not isinstance(item, dict):
            continue
        source_id, title, url = item.get("source_id"), item.get("title"), item.get("url")
        if all(isinstance(value, str) and value for value in (source_id, title, url)):
            candidates[source_id] = {"source_id": source_id, "title": title, "url": url}
    return candidates


def _source_extension(content_type: str) -> str:
    return {
        "text/html": ".html",
        "application/xhtml+xml": ".html",
        "text/plain": ".txt",
        "application/pdf": ".pdf",
    }[content_type]


def _load_batch_module():
    """Load the bundled converter modules without colliding with knowledge/convert.py."""

    global _BATCH_MODULE
    if _BATCH_MODULE is not None:
        return _BATCH_MODULE

    def load_module(name: str, path: Path):
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise WebSearchError(f"無法載入來源轉換模組：{path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        return module

    converter = load_module("_day17_source_converter", _SCRIPTS / "convert.py")
    previous_convert = sys.modules.get("convert")
    previous_validate = sys.modules.get("validate")
    sys.modules["convert"] = converter
    try:
        load_module("_day17_source_validate", _SCRIPTS / "validate.py")
        previous_alias = sys.modules.get("validate")
        sys.modules["validate"] = sys.modules["_day17_source_validate"]
        try:
            _BATCH_MODULE = load_module("_day17_source_batch", _SCRIPTS / "batch.py")
        finally:
            if previous_alias is None:
                sys.modules.pop("validate", None)
            else:
                sys.modules["validate"] = previous_alias
    finally:
        if previous_convert is None:
            sys.modules.pop("convert", None)
        else:
            sys.modules["convert"] = previous_convert
        if previous_validate is None:
            sys.modules.pop("validate", None)
        else:
            sys.modules["validate"] = previous_validate
    return _BATCH_MODULE


def _safe_title(title: str) -> str:
    title = re.sub(r"[\x00-\x1f\x7f]", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title[:240] or "web-source"


def save_and_convert_web_source(
    *,
    source_id: str,
    results_path: Path = DEFAULT_SEARCH_RESULTS,
    inbox: Path = DEFAULT_INBOX,
    raw: Path = DEFAULT_RAW,
    root: Path = PROJECT_ROOT,
    fetcher: Callable[..., tuple[bytes, str, str, str]] = fetch_url,
    converter: Callable[[Path, Path], Path] | None = None,
) -> dict[str, Any]:
    """Save one previously searched source to inbox and convert that file to raw."""

    candidate = _read_candidates(results_path).get(source_id)
    if candidate is None:
        raise WebSearchError(f"搜尋結果裡沒有來源 ID：{source_id}")
    data, final_url, content_type, charset = fetcher(
        candidate["url"],
        max_bytes=MAX_SOURCE_BYTES,
        allowed_types={"text/html", "application/xhtml+xml", "text/plain", "application/pdf"},
    )
    extension = _source_extension(content_type)
    digest = hashlib.sha256(final_url.encode("utf-8") + b"\0" + data).hexdigest()[:20]
    inbox.mkdir(parents=True, exist_ok=True)
    pending = inbox / f"web-{digest}{extension}"
    metadata_path = pending.with_name(pending.name + ".source.json")
    metadata = {
        "source_url": final_url,
        "source_name": _safe_title(candidate["title"]),
        "charset": charset,
    }
    if pending.exists() and pending.read_bytes() != data:
        raise WebSearchError(f"inbox 來源快照名稱衝突：{pending.name}")
    if metadata_path.exists():
        try:
            existing_metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise WebSearchError(f"來源中繼資料格式錯誤：{metadata_path.name}") from error
        if existing_metadata != metadata:
            raise WebSearchError(f"inbox 來源中繼資料衝突：{metadata_path.name}")
    else:
        _atomic_json(metadata_path, metadata)
    if not pending.exists():
        temporary = pending.with_name(pending.name + ".tmp")
        try:
            temporary.write_bytes(data)
            temporary.replace(pending)
        finally:
            temporary.unlink(missing_ok=True)

    if converter is None:
        batch_module = _load_batch_module()
        converter = batch_module.convert_selected_source
    output = converter(pending, root)
    raw_text = output.read_text(encoding="utf-8")
    snapshot_line = next(
        (line for line in raw_text.splitlines() if line.startswith("source_snapshot: ")),
        None,
    )
    if snapshot_line is None:
        raise WebSearchError("轉換結果缺少 source_snapshot 欄位")
    snapshot_path = json.loads(snapshot_line.partition(": ")[2])
    return {
        "source_id": source_id,
        "title": candidate["title"],
        "source_url": final_url,
        "inbox_path": snapshot_path,
        "raw_path": str(output),
        "status": "converted",
    }
