#!/usr/bin/env python3
"""Build a bounded, source-linked context from retrieved chunks."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "knowledge"))

from frontier_knowledge import DEFAULT_SYSTEM_PROMPT  # noqa: E402
from ingest import DEFAULT_TOKENIZER, Tokenizer  # noqa: E402
from retrieve import DEFAULT_DATABASE, search  # noqa: E402


Message = dict[str, str]
Candidate = dict[str, Any]


@dataclass(frozen=True)
class ContextResult:
    """The selected messages and an audit trail for every discarded candidate."""

    messages: list[Message]
    selected_chunks: list[Candidate]
    rejected_chunks: list[Candidate]
    base_input_tokens: int
    input_tokens: int
    retrieval_budget: int
    context_window: int
    output_reserve: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "messages": self.messages,
            "selected_chunks": self.selected_chunks,
            "rejected_chunks": self.rejected_chunks,
            "base_input_tokens": self.base_input_tokens,
            "input_tokens": self.input_tokens,
            "retrieval_budget": self.retrieval_budget,
            "context_window": self.context_window,
            "output_reserve": self.output_reserve,
        }


def _tool_schema_text(tool_schemas: Iterable[dict[str, Any]] | None) -> str:
    if not tool_schemas:
        return ""
    return json.dumps(
        list(tool_schemas), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )


def _system_content(
    system_prompt: str, tool_schemas: Iterable[dict[str, Any]] | None
) -> str:
    schema_text = _tool_schema_text(tool_schemas)
    if not schema_text:
        return system_prompt
    return f"{system_prompt}\n\n可用唯讀工具 schema：\n{schema_text}"


def _evidence_text(chunks: Iterable[Candidate]) -> str:
    rendered = []
    for chunk in chunks:
        location = (
            f"{chunk['source_name']}：第 {chunk['start_line']}–{chunk['end_line']} 行"
        )
        rendered.append(
            f"[{chunk['chunk_id']}] {location}\n{str(chunk['text']).rstrip()}"
        )
    return "\n\n".join(rendered)


def build_messages(
    *,
    system_prompt: str,
    question: str,
    history: Iterable[Message] | None = None,
    tool_schemas: Iterable[dict[str, Any]] | None = None,
    chunks: Iterable[Candidate] = (),
) -> list[Message]:
    """Render the exact message list whose tokens will be sent to the model."""

    messages: list[Message] = [
        {
            "role": "system",
            "content": _system_content(system_prompt, tool_schemas),
        }
    ]
    messages.extend(dict(message) for message in (history or []))
    evidence = _evidence_text(chunks)
    user_content = f"問題：{question}\n\n工程文件證據：\n"
    user_content += evidence if evidence else "（尚未選入證據）"
    messages.append({"role": "user", "content": user_content})
    return messages


def _candidate_sort_key(candidate: Candidate) -> tuple[float, str]:
    rank = candidate.get("bm25")
    try:
        numeric_rank = -float(rank) if rank is not None else float("inf")
    except (TypeError, ValueError):
        numeric_rank = float("inf")
    return numeric_rank, str(candidate.get("chunk_id", ""))


def _same_document(left: Candidate, right: Candidate) -> bool:
    return (
        left.get("document_id") == right.get("document_id")
        and left.get("source_name") == right.get("source_name")
    )


def _line_ranges_overlap(left: Candidate, right: Candidate) -> bool:
    return max(int(left["start_line"]), int(right["start_line"])) <= min(
        int(left["end_line"]), int(right["end_line"])
    )


def deduplicate_candidates(candidates: Iterable[Candidate]) -> tuple[list[Candidate], list[Candidate]]:
    """Keep the best-ranked chunk when the same document range is repeated."""

    accepted: list[Candidate] = []
    rejected: list[Candidate] = []
    seen_ids: set[str] = set()
    seen_text: set[tuple[str, str]] = set()

    for original in sorted(candidates, key=_candidate_sort_key):
        candidate = dict(original)
        chunk_id = str(candidate.get("chunk_id", ""))
        document_key = str(candidate.get("document_id", candidate.get("source_name", "")))
        text_hash = str(candidate.get("text_sha256", candidate.get("text", "")))

        if chunk_id in seen_ids:
            candidate["rejection_reason"] = "duplicate_chunk_id"
            rejected.append(candidate)
            continue
        if (document_key, text_hash) in seen_text:
            candidate["rejection_reason"] = "duplicate_text"
            rejected.append(candidate)
            continue

        overlapping = next(
            (
                selected
                for selected in accepted
                if _same_document(selected, candidate)
                and _line_ranges_overlap(selected, candidate)
            ),
            None,
        )
        if overlapping is not None:
            candidate["rejection_reason"] = (
                f"overlapping_lines_with:{overlapping['chunk_id']}"
            )
            rejected.append(candidate)
            continue

        accepted.append(candidate)
        seen_ids.add(chunk_id)
        seen_text.add((document_key, text_hash))

    return accepted, rejected


def build_context(
    *,
    tokenizer: Any,
    candidates: Iterable[Candidate],
    question: str,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    history: Iterable[Message] | None = None,
    tool_schemas: Iterable[dict[str, Any]] | None = None,
    context_window: int,
    output_reserve: int,
) -> ContextResult:
    """Select complete chunks without exceeding input plus output budget."""

    if context_window <= 0:
        raise ValueError("context_window 必須大於 0")
    if output_reserve < 0:
        raise ValueError("output_reserve 不可小於 0")
    if output_reserve >= context_window:
        raise ValueError("output_reserve 必須小於 context_window")

    deduplicated, duplicate_rejections = deduplicate_candidates(candidates)
    base_messages = build_messages(
        system_prompt=system_prompt,
        question=question,
        history=history,
        tool_schemas=tool_schemas,
    )
    base_input_tokens = int(tokenizer.chat_count(base_messages))
    retrieval_budget = context_window - output_reserve - base_input_tokens

    selected: list[Candidate] = []
    budget_rejections: list[Candidate] = []
    input_tokens = base_input_tokens
    for index, candidate in enumerate(deduplicated):
        trial_messages = build_messages(
            system_prompt=system_prompt,
            question=question,
            history=history,
            tool_schemas=tool_schemas,
            chunks=[*selected, candidate],
        )
        trial_tokens = int(tokenizer.chat_count(trial_messages))
        if trial_tokens + output_reserve > context_window:
            rejected_candidate = dict(candidate)
            rejected_candidate["rejection_reason"] = "context_budget"
            budget_rejections.append(rejected_candidate)
            if selected:
                for remainder in deduplicated[index + 1 :]:
                    remainder_copy = dict(remainder)
                    remainder_copy["rejection_reason"] = "context_budget_after_stop"
                    budget_rejections.append(remainder_copy)
                break
            continue
        selected.append(candidate)
        input_tokens = trial_tokens

    messages = build_messages(
        system_prompt=system_prompt,
        question=question,
        history=history,
        tool_schemas=tool_schemas,
        chunks=selected,
    )
    return ContextResult(
        messages=messages,
        selected_chunks=selected,
        rejected_chunks=[*duplicate_rejections, *budget_rejections],
        base_input_tokens=base_input_tokens,
        input_tokens=input_tokens,
        retrieval_budget=retrieval_budget,
        context_window=context_window,
        output_reserve=output_reserve,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="從 FTS5 候選 chunks 組出受 context budget 限制的 evidence context。"
    )
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--tokenizer", default=None)
    parser.add_argument("--query", required=True, help="先交給 SQLite FTS5 的查詢字串")
    parser.add_argument("--question", default=None, help="送給模型的問題；省略時沿用 query")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--context-window", type=int, default=1024)
    parser.add_argument("--output-reserve", type=int, default=128)
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        matches = search(
            args.database,
            args.query,
            limit=args.limit,
        )
        tokenizer = Tokenizer(args.tokenizer or DEFAULT_TOKENIZER)
        result = build_context(
            tokenizer=tokenizer,
            candidates=matches,
            question=args.question or args.query,
            system_prompt=args.system_prompt,
            context_window=args.context_window,
            output_reserve=args.output_reserve,
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
        print(f"context 組裝失敗：{error}", file=sys.stderr)
        return 1

    print(
        f"候選 {len(matches)} 個；去重後選入 {len(result.selected_chunks)} 個，"
        f"淘汰 {len(result.rejected_chunks)} 個"
    )
    print(
        f"base input tokens={result.base_input_tokens}，"
        f"retrieval budget={result.retrieval_budget}，"
        f"final input tokens={result.input_tokens}，"
        f"output reserve={result.output_reserve}"
    )
    for index, chunk in enumerate(result.selected_chunks, start=1):
        print(
            f"{index}. {chunk['source_name']}（第 {chunk['start_line']}–"
            f"{chunk['end_line']} 行，{chunk['chunk_id']}）"
        )
    for chunk in result.rejected_chunks:
        print(f"淘汰：{chunk['chunk_id']}（{chunk['rejection_reason']}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
