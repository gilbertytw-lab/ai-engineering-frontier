#!/usr/bin/env python3
"""Measure the local model's first tool choice without executing any tool."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "knowledge"))

from frontier_knowledge import DEFAULT_BASE_URL  # noqa: E402
from tools import SYSTEM_PROMPT, TOOL_SCHEMAS, _choice, _prior_search_context, call_completion  # noqa: E402


DEFAULT_MODEL = "mlx-community/Qwen3.8-27B-4bit"
DEFAULT_CASES = PROJECT_ROOT / "knowledge" / "routing_cases.json"


def load_cases(path: Path) -> list[dict[str, Any]]:
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise ValueError("路由案例必須是非空陣列")
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("每個路由案例都必須是 object")
        if not isinstance(case.get("id"), str) or not case["id"].strip():
            raise ValueError("每個路由案例都需要 id")
        if not isinstance(case.get("question"), str) or not case["question"].strip():
            raise ValueError(f"案例 {case.get('id')} 缺少 question")
        if case.get("expected_tool") is not None and not isinstance(case["expected_tool"], str):
            raise ValueError(f"案例 {case['id']} 的 expected_tool 必須是字串或 null")
        search_results = case.get("search_results", [])
        if not isinstance(search_results, list):
            raise ValueError(f"案例 {case['id']} 的 search_results 必須是陣列")
    return cases


def capture_choice(
    case: dict[str, Any], *, base_url: str, model: str | None
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="day18-routing-") as temporary_dir:
        results_path = Path(temporary_dir) / "search-results.json"
        search_results = case.get("search_results", [])
        if search_results:
            results_path.write_text(
                json.dumps({"version": 1, "results": search_results}, ensure_ascii=False),
                encoding="utf-8",
            )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": case["question"] + _prior_search_context(results_path),
            },
        ]
        started = time.perf_counter()
        completion = call_completion(
            messages,
            base_url=base_url,
            model=model,
            max_tokens=256,
            tools=TOOL_SCHEMAS,
        )
        elapsed_ms = round((time.perf_counter() - started) * 1000, 1)

    finish_reason, message = _choice(completion)
    tool_calls = message.get("tool_calls") or []
    if not isinstance(tool_calls, list):
        raise ValueError("runtime 的 tool_calls 必須是陣列")
    selected_tools = []
    selected_arguments = []
    for tool_call in tool_calls:
        function = tool_call.get("function") if isinstance(tool_call, dict) else None
        selected_tools.append(function.get("name") if isinstance(function, dict) else None)
        selected_arguments.append(
            function.get("arguments") if isinstance(function, dict) else None
        )
    expected_tool = case["expected_tool"]
    is_match = selected_tools == ([] if expected_tool is None else [expected_tool])
    return {
        "case_id": case["id"],
        "category": case.get("category", "uncategorized"),
        "expected_tool": expected_tool,
        "selected_tools": selected_tools,
        "selected_arguments": selected_arguments,
        "finish_reason": finish_reason,
        "is_match": is_match,
        "elapsed_ms": elapsed_ms,
        "usage": completion.get("usage", {}),
    }


def summarize(results: list[dict[str, Any]]) -> dict[str, Any]:
    completed = [result for result in results if "error" not in result]
    correct = sum(result["is_match"] for result in completed)
    false_tool = sum(
        result["expected_tool"] is None and bool(result["selected_tools"])
        for result in completed
    )
    missed_tool = sum(
        result["expected_tool"] is not None and not result["selected_tools"]
        for result in completed
    )
    wrong_tool = sum(
        result["expected_tool"] is not None
        and result["selected_tools"]
        and result["selected_tools"] != [result["expected_tool"]]
        for result in completed
    )
    return {
        "case_count": len(results),
        "completed_count": len(completed),
        "error_count": len(results) - len(completed),
        "correct_count": correct,
        "exact_match_rate": round(correct / len(completed), 3) if completed else None,
        "false_tool_count": false_tool,
        "missed_tool_count": missed_tool,
        "wrong_tool_count": wrong_tool,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="量測 Qwen 首次選擇的工具；本程式不執行工具。"
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.cases)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"無法讀取路由案例：{error}", file=sys.stderr)
        return 1

    output_path = args.output
    if output_path is None:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_path = PROJECT_ROOT / "runs" / f"day18-routing-{stamp}.jsonl"
    elif not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    with output_path.open("w", encoding="utf-8") as output:
        output.write(
            json.dumps(
                {
                    "record_type": "run",
                    "model": args.model,
                    "base_url": args.base_url,
                    "case_count": len(cases),
                    "tool_execution": False,
                },
                ensure_ascii=False,
            )
            + "\n"
        )
        for case in cases:
            try:
                record = capture_choice(case, base_url=args.base_url, model=args.model)
            except (OSError, RuntimeError, TypeError, ValueError) as error:
                record = {
                    "case_id": case["id"],
                    "category": case.get("category", "uncategorized"),
                    "expected_tool": case["expected_tool"],
                    "error": f"{type(error).__name__}: {error}",
                }
            records.append(record)
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
            output.flush()
            print(
                f"{record['case_id']}：expected={record['expected_tool']}，"
                f"selected={record.get('selected_tools', [])}，"
                f"{'PASS' if record.get('is_match') else 'ERROR' if 'error' in record else 'MISMATCH'}"
            )

        summary = summarize(records)
        output.write(
            json.dumps({"record_type": "summary", **summary}, ensure_ascii=False) + "\n"
        )

    print(json.dumps(summary, ensure_ascii=False))
    print(f"紀錄：{output_path}")
    return 0 if summary["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
