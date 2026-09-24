#!/usr/bin/env python3
"""Measure local-model latency at a few bounded evidence sizes."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "knowledge"))

from frontier_knowledge import DEFAULT_BASE_URL, DEFAULT_SYSTEM_PROMPT, call_local_model  # noqa: E402
from ingest import DEFAULT_MANIFEST, DEFAULT_TOKENIZER, Tokenizer  # noqa: E402


def load_manifest(path: Path) -> dict[str, Any]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict) or not isinstance(manifest.get("documents"), list):
        raise ValueError(f"manifest 格式不正確：{path}")
    return manifest


def select_chunks(
    manifest: dict[str, Any],
    *,
    document_id: str | None,
    evidence_tokens: int,
) -> list[dict[str, Any]]:
    if evidence_tokens <= 0:
        raise ValueError("evidence_tokens 必須大於 0")
    documents = manifest["documents"]
    if document_id:
        documents = [doc for doc in documents if doc.get("document_id") == document_id]
        if not documents:
            raise ValueError(f"manifest 找不到 document_id：{document_id}")

    selected: list[dict[str, Any]] = []
    total = 0
    for document in documents:
        for chunk in document.get("chunks", []):
            count = int(chunk["token_count"])
            if selected and total + count > evidence_tokens:
                return selected
            selected.append(chunk)
            total += count
            if total >= evidence_tokens:
                return selected
    return selected


def build_prompt(question: str, chunks: list[dict[str, Any]]) -> str:
    evidence = "\n\n".join(
        f"[{chunk['chunk_id']}]\n{chunk['text'].rstrip()}" for chunk in chunks
    )
    return (
        "請只根據下列工程文件證據回答問題。若證據不足，請明確回答不知道，"
        "不要使用文件以外的常識補齊。回答最後列出使用到的 chunk_id。\n\n"
        f"問題：{question}\n\n"
        f"工程文件證據：\n{evidence}"
    )


def measure_once(
    *,
    question: str,
    chunks: list[dict[str, Any]],
    tokenizer: Tokenizer,
    base_url: str,
    model: str | None,
    system_prompt: str,
    max_tokens: int,
    dry_run: bool,
    enable_thinking: bool,
) -> dict[str, Any]:
    prompt = build_prompt(question, chunks)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    input_tokens = tokenizer.chat_count(messages)
    evidence_tokens = sum(int(chunk["token_count"]) for chunk in chunks)
    result: dict[str, Any] = {
        "evidence_tokens": evidence_tokens,
        "input_tokens": input_tokens,
        "chunk_ids": [chunk["chunk_id"] for chunk in chunks],
        "enable_thinking": enable_thinking,
        "status": "planned" if dry_run else "pending",
    }
    if dry_run:
        return result

    started = time.perf_counter()
    answer = call_local_model(
        prompt,
        base_url=base_url,
        model=model,
        system_prompt=system_prompt,
        temperature=0,
        max_tokens=max_tokens,
        chat_template_kwargs={"enable_thinking": enable_thinking},
    )
    elapsed_ms = round((time.perf_counter() - started) * 1000, 1)
    result.update(
        {
            "status": "ok",
            "elapsed_ms": elapsed_ms,
            "output_tokens_estimate": tokenizer.count(answer),
            "answer_preview": answer.replace("\n", " ").strip()[:160],
        }
    )
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="以固定問題量測不同證據大小下的本地 Qwen 輸入 token 與延遲。"
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--tokenizer", default=None)
    parser.add_argument("--document-id")
    parser.add_argument(
        "--question",
        default="production release 前，最少要檢查哪些事項？如果資料不足，請明確說不知道。",
    )
    parser.add_argument("--evidence-tokens", nargs="+", type=int, default=[192, 384, 768])
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--model", default=None)
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--max-tokens", type=int, default=128)
    parser.add_argument(
        "--enable-thinking",
        action="store_true",
        help="保留 Qwen reasoning；預設關閉，讓 max_tokens 主要留給可讀回答。",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = load_manifest(args.manifest)
        tokenizer_name = args.tokenizer or manifest.get("tokenizer") or DEFAULT_TOKENIZER
        tokenizer = Tokenizer(tokenizer_name)
        for evidence_tokens in args.evidence_tokens:
            chunks = select_chunks(
                manifest,
                document_id=args.document_id,
                evidence_tokens=evidence_tokens,
            )
            if not chunks:
                raise ValueError(f"找不到可用 chunks：evidence_tokens={evidence_tokens}")
            result = measure_once(
                question=args.question,
                chunks=chunks,
                tokenizer=tokenizer,
                base_url=args.base_url,
                model=args.model,
                system_prompt=args.system_prompt,
                max_tokens=args.max_tokens,
                dry_run=args.dry_run,
                enable_thinking=args.enable_thinking,
            )
            result["requested_evidence_tokens"] = evidence_tokens
            print(json.dumps(result, ensure_ascii=False))
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
        print(f"量測失敗：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
