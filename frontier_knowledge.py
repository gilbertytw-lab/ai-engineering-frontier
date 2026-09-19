#!/usr/bin/env python3
"""Send one prompt or run an interactive session with a local model server."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "http://127.0.0.1:8081/v1"
DEFAULT_SYSTEM_PROMPT = (
    "你是本地工程知識助理。請用繁體中文直接回答問題，先給結論，再補充必要說明。"
    "資訊不足時，請明確說明不知道，不要自行捏造。"
)
EXIT_COMMANDS = frozenset({":q", "exit", "quit"})
JSON_ANSWER_PROMPT = (
    '只輸出一個 JSON object，恰好包含 "answer" 和 "limitations" 兩個欄位。'
    'answer 是非空白字串；limitations 是字串陣列，每個項目都不可為空白。'
    '資訊不足時在 answer 說明不知道，並在 limitations 說明缺少什麼；'
    '沒有要補充的限制時使用空陣列 []。不要加 Markdown 程式碼圍欄或 JSON 以外的文字。'
)


def parse_answer(content: str) -> dict[str, object]:
    """Validate this project's two-field answer contract."""

    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"重複欄位：{key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"不接受 JSON 常數：{value}")

    try:
        answer = json.loads(
            content, object_pairs_hook=unique_object, parse_constant=reject_constant
        )
    except ValueError as error:
        raise RuntimeError(f"回答不是可接受的 JSON：{error}") from error
    if not isinstance(answer, dict) or set(answer) != {"answer", "limitations"}:
        raise RuntimeError("回答必須恰好包含 answer 和 limitations 兩個欄位")
    if not isinstance(answer["answer"], str) or not answer["answer"].strip():
        raise RuntimeError("answer 必須是非空白字串")
    limitations = answer["limitations"]
    if not isinstance(limitations, list) or any(
        not isinstance(item, str) or not item.strip() for item in limitations
    ):
        raise RuntimeError("limitations 必須是非空白字串組成的陣列，可以為空陣列")
    return answer


def build_messages(prompt: str, system_prompt: str | None) -> list[dict[str, str]]:
    """Build the chat messages sent to the local runtime."""

    messages: list[dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    return messages


def call_local_model(
    prompt: str,
    *,
    base_url: str,
    model: str | None,
    system_prompt: str | None,
    temperature: float,
    max_tokens: int,
    json_answer: bool = False,
) -> str:
    """Call the local chat-completions endpoint and return the answer text."""

    if json_answer:
        system_prompt = "\n".join(filter(None, [system_prompt, JSON_ANSWER_PROMPT]))
    payload: dict[str, object] = {
        "messages": build_messages(prompt, system_prompt),
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if model:
        payload["model"] = model

    request = Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=120) as response:
            result = json.load(response)
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"runtime 回傳 HTTP {error.code}：{detail}") from error
    except URLError as error:
        raise RuntimeError(
            "連不到本地 runtime。請先啟動 mlx_lm.server，並確認網址是 "
            f"{base_url}。"
        ) from error

    try:
        content = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError(f"runtime 回傳格式與預期不同：{result}") from error
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("runtime 未回傳非空白的 message.content")
    if json_answer:
        return json.dumps(parse_answer(content), ensure_ascii=False, indent=2)
    return content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="從本地 runtime 取得一次回答，或啟動互動式 Chat Runner。"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="要送給本地模型的問題；省略後進入互動模式",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="明確啟動互動模式",
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("LOCAL_RUNTIME_URL", DEFAULT_BASE_URL),
        help=f"runtime 的 API 位址（預設：{DEFAULT_BASE_URL}）",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("LOCAL_MODEL"),
        help="模型名稱；mlx_lm.server 通常可以省略",
    )
    system_prompt_group = parser.add_mutually_exclusive_group()
    system_prompt_group.add_argument(
        "--system-prompt",
        default=os.getenv("LOCAL_SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT),
        help="送給模型的固定 system message",
    )
    system_prompt_group.add_argument(
        "--no-system-prompt",
        action="store_true",
        help="不要加入 Day 4 的預設 system message，方便比較差異",
    )
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=256)
    parser.add_argument("--json-answer", action="store_true", help="要求並驗證 JSON 回答格式")
    args = parser.parse_args()
    if args.interactive and args.prompt is not None:
        parser.error("--interactive 不可和單次 prompt 同時使用")
    if args.json_answer and args.no_system_prompt:
        parser.error("--json-answer 需要 system 格式指令，不可和 --no-system-prompt 同時使用")
    return args


def run_interactive(
    *,
    base_url: str,
    model: str | None,
    system_prompt: str | None,
    temperature: float,
    max_tokens: int,
    json_answer: bool = False,
) -> int:
    """Read prompts until the user exits, keeping each request independent."""

    print("已進入互動模式。輸入 exit、quit 或 :q 結束。")
    while True:
        try:
            prompt = input("你 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已結束本次互動。")
            return 0

        if not prompt:
            continue
        if prompt.casefold() in EXIT_COMMANDS:
            print("已結束本次互動。")
            return 0

        try:
            answer = call_local_model(
                prompt,
                base_url=base_url,
                model=model,
                system_prompt=system_prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                json_answer=json_answer,
            )
        except RuntimeError as error:
            print(f"錯誤：{error}", file=sys.stderr)
            continue

        print(f"模型 > {answer}")


def main() -> int:
    args = parse_args()
    system_prompt = None if args.no_system_prompt else args.system_prompt

    if args.interactive or args.prompt is None:
        return run_interactive(
            base_url=args.base_url,
            model=args.model,
            system_prompt=system_prompt,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            json_answer=args.json_answer,
        )

    try:
        answer = call_local_model(
            args.prompt,
            base_url=args.base_url,
            model=args.model,
            system_prompt=system_prompt,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            json_answer=args.json_answer,
        )
    except RuntimeError as error:
        print(f"錯誤：{error}", file=sys.stderr)
        return 1

    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
