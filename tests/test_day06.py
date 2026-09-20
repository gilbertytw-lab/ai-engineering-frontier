import contextlib
import io
import unittest
from unittest.mock import patch

import frontier_knowledge as runner


class SessionHistoryTests(unittest.TestCase):
    def test_build_messages_places_history_between_system_and_current_user(self):
        history = [
            {"role": "user", "content": "記住代號：港口 17"},
            {"role": "assistant", "content": "收到"},
        ]

        messages = runner.build_messages("代號是什麼？", "固定規則", history)

        self.assertEqual(
            messages,
            [
                {"role": "system", "content": "固定規則"},
                {"role": "user", "content": "記住代號：港口 17"},
                {"role": "assistant", "content": "收到"},
                {"role": "user", "content": "代號是什麼？"},
            ],
        )
        self.assertEqual(history[0]["content"], "記住代號：港口 17")

    def test_interactive_reuses_successful_turns(self):
        with patch(
            "builtins.input", side_effect=["記住代號：港口 17", "代號是什麼？", "exit"]
        ), patch.object(
            runner, "call_local_model", side_effect=["收到", "港口 17"]
        ) as call, contextlib.redirect_stdout(io.StringIO()):
            result = runner.run_interactive(
                base_url="test",
                model=None,
                system_prompt="規則",
                temperature=0.2,
                max_tokens=1024,
            )

        self.assertEqual(result, 0)
        self.assertEqual(call.call_args_list[0].kwargs["history"], [])
        self.assertEqual(
            call.call_args_list[1].kwargs["history"],
            [
                {"role": "user", "content": "記住代號：港口 17"},
                {"role": "assistant", "content": "收到"},
            ],
        )

    def test_failed_turn_is_not_added_to_history(self):
        with patch(
            "builtins.input", side_effect=["失敗題", "成功題", "exit"]
        ), patch.object(
            runner,
            "call_local_model",
            side_effect=[RuntimeError("格式錯誤"), "成功回答"],
        ) as call, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
            io.StringIO()
        ):
            runner.run_interactive(
                base_url="test",
                model=None,
                system_prompt="規則",
                temperature=0.2,
                max_tokens=1024,
            )

        self.assertEqual(call.call_args_list[1].kwargs["history"], [])

    def test_no_history_keeps_requests_independent(self):
        with patch(
            "builtins.input", side_effect=["第一題", "第二題", "exit"]
        ), patch.object(
            runner, "call_local_model", side_effect=["第一答", "第二答"]
        ) as call, contextlib.redirect_stdout(io.StringIO()):
            runner.run_interactive(
                base_url="test",
                model=None,
                system_prompt="規則",
                temperature=0.2,
                max_tokens=1024,
                keep_history=False,
            )

        self.assertIsNone(call.call_args_list[0].kwargs["history"])
        self.assertIsNone(call.call_args_list[1].kwargs["history"])

    def test_cli_rejects_no_history_for_single_prompt(self):
        with patch("sys.argv", ["runner", "--no-history", "問題"]), contextlib.redirect_stderr(
            io.StringIO()
        ), self.assertRaises(SystemExit) as error:
            runner.parse_args()

        self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
