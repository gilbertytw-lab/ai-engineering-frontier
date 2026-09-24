#!/usr/bin/env python3
"""Convert whole text files, text-layer PDFs, and static pages to source-linked Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

VERSION = "0.3.0"
MAX_SOURCE_BYTES = 100 * 1024 * 1024  # File safety limit, unrelated to model context.


@dataclass(frozen=True)
class Source:
    data: bytes
    name: str
    kind: str
    format: str
    suffix: str
    charset: str = "utf-8"
    url: str | None = None


@dataclass(frozen=True)
class Extraction:
    body: str
    identity_text: str
    pages: int | None = None


class PageText(HTMLParser):
    BLOCKS = {"article", "blockquote", "br", "dd", "div", "dt", "h1", "h2", "h3", "h4", "h5", "h6", "li", "p", "pre", "section", "table", "td", "th", "title", "tr", "ul", "ol"}
    SKIP = {"script", "style", "noscript", "svg"}
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, base_url: str, focus_class: str | None = None) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.focus_class = focus_class
        self.focus_depth = 0
        self.found_focus = False
        self.parts: list[str] = []
        self.skip_depth = 0
        self.links: list[str | None] = []
        self.in_pre = False
        self.code_blocks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.focus_class:
            if self.focus_depth:
                if tag not in self.VOID:
                    self.focus_depth += 1
            elif self.focus_class in (dict(attrs).get("class") or "").split():
                self.focus_depth = 1
                self.found_focus = True
            else:
                return
        if tag in self.SKIP:
            self.skip_depth += 1
        if self.skip_depth:
            return
        if tag == "pre":
            self.in_pre = True
            self.code_blocks.append("")
            self.parts.append(f"\n\n__RAW_MD_CODE_BLOCK_{len(self.code_blocks) - 1}__\n\n")
            return
        if self.in_pre:
            if tag == "br":
                self.code_blocks[-1] += "\n"
            return
        if re.fullmatch(r"h[1-6]", tag) and self.focus_class != "qa-header__title":
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag in self.BLOCKS:
            self.parts.append("\n")
        if tag == "a":
            href = dict(attrs).get("href")
            self.links.append(urljoin(self.base_url, href) if href else None)

    def handle_endtag(self, tag: str) -> None:
        if self.focus_class and not self.focus_depth:
            return
        if tag in self.SKIP and self.skip_depth:
            self.skip_depth -= 1
        elif tag == "pre" and self.in_pre:
            self.in_pre = False
        elif not self.skip_depth:
            if self.in_pre:
                pass
            elif tag == "a" and self.links:
                href = self.links.pop()
                if href:
                    self.parts.append(f" ({href})")
            if not self.in_pre and tag in self.BLOCKS:
                self.parts.append("\n")
        if self.focus_class and tag not in self.VOID:
            self.focus_depth -= 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if not self.skip_depth and (not self.focus_class or self.focus_depth):
            if self.in_pre:
                self.code_blocks[-1] += data
            else:
                self.parts.append(data)

    def text(self) -> str:
        value = "".join(self.parts)
        value = re.sub(r"[\t \f\v]+", " ", value)
        value = re.sub(r" *\n *", "\n", value)
        value = re.sub(r"\n{3,}", "\n\n", value).strip()
        for number, code in enumerate(self.code_blocks):
            fence = "`" * max(3, max((len(match.group()) for match in re.finditer(r"`+", code)), default=0) + 1)
            value = value.replace(f"__RAW_MD_CODE_BLOCK_{number}__", f"{fence}\n{code.strip(chr(10))}\n{fence}")
        return value


class DeclaredPageURL(HTMLParser):
    """Read a page's declared URL only to select its static article body."""

    def __init__(self) -> None:
        super().__init__()
        self.url: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "meta" or self.url:
            return
        values = dict(attrs)
        candidate = values.get("content") if values.get("property") == "og:url" else None
        if candidate and urlsplit(candidate).scheme in {"http", "https"}:
            self.url = candidate


def read_source(source_arg: str) -> Source:
    url = urlsplit(source_arg)
    if url.scheme in {"http", "https"}:
        if url.username or url.password:
            raise ValueError("網址不可包含帳號或密碼")
        request = Request(source_arg, headers={"User-Agent": f"source-to-raw-md/{VERSION}"})
        try:
            with urlopen(request, timeout=30) as response:
                final_url = response.geturl()
                if urlsplit(final_url).scheme not in {"http", "https"}:
                    raise ValueError("重新導向後的網址不是 HTTP 或 HTTPS")
                content_type = response.headers.get_content_type()
                charset = response.headers.get_content_charset() or "utf-8"
                data = response.read(MAX_SOURCE_BYTES + 1)
        except (HTTPError, URLError) as error:
            raise RuntimeError(f"無法下載網頁：{error}") from error
        if len(data) > MAX_SOURCE_BYTES:
            raise ValueError("來源超過 100 MiB 的檔案安全上限")
        if content_type in {"text/html", "application/xhtml+xml"}:
            return Source(data, source_arg, "web", "html", ".html", charset, final_url)
        if content_type == "application/pdf":
            return Source(data, source_arg, "pdf", "pdf", ".pdf", url=final_url)
        if content_type == "text/plain":
            return Source(data, source_arg, "text", "txt", ".txt", charset, final_url)
        raise ValueError(f"網頁內容格式不支援：{content_type}")
    if url.scheme:
        raise ValueError("來源必須是本機檔案或 HTTP/HTTPS 網址")
    path = Path(source_arg).expanduser()
    if not path.is_file():
        raise ValueError(f"找不到來源檔：{path}")
    formats = {".txt": ("text", "txt"), ".md": ("text", "md"), ".markdown": ("text", "markdown"), ".pdf": ("pdf", "pdf"), ".html": ("web", "html"), ".htm": ("web", "html")}
    suffix = path.suffix.lower()
    if suffix not in formats:
        raise ValueError(f"檔案格式不支援：{suffix}")
    if path.stat().st_size > MAX_SOURCE_BYTES:
        raise ValueError("來源超過 100 MiB 的檔案安全上限")
    kind, format_name = formats[suffix]
    return Source(path.read_bytes(), path.name, kind, format_name, suffix)


def document_id(source: Source, extracted_text: str) -> str:
    content = extracted_text.encode("utf-8") if source.kind == "web" else source.data
    identity = (source.url or source.name).encode("utf-8")
    return f"doc-{hashlib.sha256(identity + b'\0' + content).hexdigest()[:16]}"


def extract(source: Source) -> Extraction:
    if source.format == "pdf":
        try:
            from pypdf import PdfReader
        except ImportError as error:
            raise RuntimeError("PDF 需要 pypdf；請先執行 uv run --with pypdf") from error
        try:
            reader = PdfReader(BytesIO(source.data), strict=True)
            pages = [page.extract_text() or "" for page in reader.pages]
        except Exception as error:
            raise RuntimeError(f"PDF 文字抽取失敗：{error}") from error
        if not pages:
            raise ValueError("PDF 沒有頁面")
        empty = [number for number, page in enumerate(pages, 1) if not page.strip()]
        if empty:
            raise ValueError(f"PDF 第 {', '.join(map(str, empty))} 頁沒有可抽取的文字；可能需要 OCR，未寫入 raw")
        # No per-page or total character limit: every page enters the output.
        body = f"# {Path(source.name).stem}\n\n" + "\n\n".join(
            f"## 第 {number} 頁\n\n{page.strip()}" for number, page in enumerate(pages, 1)
        ) + "\n"
        return Extraction(body, "\n\n".join(pages), len(pages))
    try:
        source_text = source.data.decode(source.charset if source.kind == "web" else "utf-8-sig")
    except (UnicodeError, LookupError) as error:
        raise ValueError(f"來源文字編碼無法讀取：{error}") from error
    if source.format == "html":
        origin = DeclaredPageURL()
        origin.feed(source_text)
        page_url = source.url or origin.url or ""
        if urlsplit(page_url).hostname == "ithelp.ithome.com.tw":
            title = PageText(page_url, "qa-header__title")
            body = PageText(page_url, "markdown__style")
            title.feed(source_text)
            body.feed(source_text)
            if not title.found_focus or not body.found_focus:
                raise ValueError("iT 邦幫忙文章結構已改變；未將導覽文字當成正文")
            extracted = f"{title.text()}\n\n{body.text()}"
        else:
            parser = PageText(page_url)
            parser.feed(source_text)
            extracted = parser.text()
        if not extracted.strip():
            raise ValueError("網頁沒有可轉換的文字")
        first, _, rest = extracted.partition("\n")
        markdown = f"# {first.strip()}\n\n{rest.strip()}\n" if rest.strip() else f"# {first.strip()}\n"
        return Extraction(markdown, extracted)
    if not source_text.strip():
        raise ValueError("來源沒有可轉換的文字")
    if source.format in {"md", "markdown"}:
        body = source_text.lstrip("\ufeff")
    else:
        body = f"# {Path(source.name).stem}\n\n{source_text}"
    return Extraction(body.rstrip("\n") + "\n", source_text)


def snapshot_source(source_arg: str, source: Source, source_dir: Path, doc_id: str) -> Path:
    source_dir = source_dir.resolve()
    source_dir.mkdir(parents=True, exist_ok=True)
    input_path = Path(source_arg).expanduser().resolve() if not source.url else None
    if input_path and input_path.is_relative_to(source_dir):
        return input_path
    filename = f"{doc_id}-{hashlib.sha256(source.data).hexdigest()[:12]}{source.suffix}" if source.url else f"{doc_id}-{Path(source_arg).name}"
    target = source_dir / filename
    if target.exists():
        if target.read_bytes() != source.data:
            raise RuntimeError(f"來源快照同名但內容不同：{target}")
    else:
        target.write_bytes(source.data)
    return target


def render_markdown(source: Source, extraction: Extraction, doc_id: str, snapshot: Path) -> str:
    try:
        snapshot_name = snapshot.relative_to(Path.cwd()).as_posix()
    except ValueError:
        snapshot_name = snapshot.as_posix()
    fields = {
        "document_id": doc_id,
        "source_name": source.name,
        "source_type": source.kind,
        "source_format": source.format,
        "source_sha256": hashlib.sha256(source.data).hexdigest(),
        "source_snapshot": snapshot_name,
        "extracted_sha256": hashlib.sha256(extraction.identity_text.encode("utf-8")).hexdigest(),
        "conversion_method": "programmatic",
        "converter_version": VERSION,
    }
    if source.url:
        fields["source_url"] = source.url
    if source.charset.lower() != "utf-8" and source.format != "pdf":
        fields["source_charset"] = source.charset
    if extraction.pages is not None:
        fields["pdf_pages"] = extraction.pages
        fields["extraction_scope"] = "PDF text layer; page order preserved; figures and layout require source review"
    header = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    return f"---\n{header}\n---\n\n{extraction.body}"


def convert(source_arg: str, source_dir: Path, output_dir: Path) -> Path:
    if source_dir.resolve() == output_dir.resolve():
        raise ValueError("原檔目錄與 raw 輸出目錄不可相同")
    source = read_source(source_arg)
    extraction = extract(source)
    doc_id = document_id(source, extraction.identity_text)
    output = output_dir / f"{doc_id}.md"
    if output.exists():
        existing = output.read_text(encoding="utf-8")
        content_field = (
            f'extracted_sha256: "{hashlib.sha256(extraction.identity_text.encode("utf-8")).hexdigest()}"'
            if source.kind == "web" else f'source_sha256: "{hashlib.sha256(source.data).hexdigest()}"'
        )
        if all(field in existing for field in (f'document_id: "{doc_id}"', content_field,
                                               'conversion_method: "programmatic"', f'converter_version: "{VERSION}"')):
            snapshot = snapshot_source(source_arg, source, source_dir, doc_id)
            desired = render_markdown(source, extraction, doc_id, snapshot)
            if existing != desired:
                old_snapshot = re.search(r'^source_snapshot: .+$', existing, flags=re.M)
                new_snapshot = re.search(r'^source_snapshot: .+$', desired, flags=re.M)
                if (old_snapshot and new_snapshot and
                        existing.replace(old_snapshot.group(), new_snapshot.group(), 1) == desired):
                    temporary = output.with_suffix(".md.tmp")
                    try:
                        temporary.write_text(desired, encoding="utf-8", newline="\n")
                        os.replace(temporary, output)
                    finally:
                        temporary.unlink(missing_ok=True)
                elif source.kind != "web" or f'source_sha256: "{hashlib.sha256(source.data).hexdigest()}"' in existing:
                    raise RuntimeError(f"raw 檔內容與來源不一致：{output}")
            return output
        raise RuntimeError(f"raw 檔已存在但格式或來源版本不同：{output}；請先保留舊版並另選輸出目錄")
    snapshot = snapshot_source(source_arg, source, source_dir, doc_id)
    rendered = render_markdown(source, extraction, doc_id, snapshot)
    output_dir.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".md.tmp")
    try:
        temporary.write_text(rendered, encoding="utf-8", newline="\n")
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="不呼叫模型，將完整文字、可抽字 PDF 或靜態網頁轉成帶來源欄位的 raw Markdown。")
    parser.add_argument("source", help="本機 .txt/.md/.pdf/.html 檔或 HTTP/HTTPS 網址")
    parser.add_argument("--source-dir", type=Path, default=Path("knowledge/inbox"), help="保存原始來源的目錄")
    parser.add_argument("--output-dir", type=Path, default=Path("knowledge/raw"), help="標準化 Markdown 輸出目錄")
    args = parser.parse_args()
    try:
        output = convert(args.source, args.source_dir, args.output_dir)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"轉換失敗：{error}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
