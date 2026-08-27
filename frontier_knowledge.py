#!/usr/bin/env python3
"""Day 2: send one prompt to a local OpenAI-compatible model server."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "http://127.0.0.1:8080/v1"


def call_local_model(
    prompt: str,
    *,
    base_url: str,
    model: str | None,
    temperature: float,
    max_tokens: int,
) -> str:
    """Call the local chat-completions endpoint and return the answer text."""

    payload: dict[str, object] = {
        "messages": [{"role": "user", "content": prompt}],
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
        return result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError(f"runtime 回傳格式與預期不同：{result}") from error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="從本地 runtime 取得一次模型回答。"
    )
    parser.add_argument("prompt", help="要送給本地模型的問題")
    parser.add_argument(
        "--base-url",
        default=os.getenv("LOCAL_RUNTIME_URL", DEFAULT_BASE_URL),
        help=f"runtime 的 API 位址（預設：{DEFAULT_BASE_URL}）",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("LOCAL_MODEL"),
        help="模型名稱；mlx-lm.server 通常可以省略",
    )
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=256)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        answer = call_local_model(
            args.prompt,
            base_url=args.base_url,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
    except RuntimeError as error:
        print(f"錯誤：{error}", file=sys.stderr)
        return 1

    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
