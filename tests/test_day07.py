import contextlib
import io
import json
import unittest
from unittest.mock import patch

import frontier_knowledge as runner


class ChatCheckpointTests(unittest.TestCase):
    def test_checkpoint_reuses_first_structured_answer(self):
        first = json.dumps({"answer": "收到", "limitations": []}, ensure_ascii=False)
        second = json.dumps(
            {"answer": runner.CHECKPOINT_CODE, "limitations": []}, ensure_ascii=False
        )

        with patch.object(
            runner, "call_local_model", side_effect=[first, second]
        ) as call, contextlib.redirect_stdout(io.StringIO()) as stdout:
            result = runner.run_checkpoint(
                base_url="test",
                model="test-model",
                system_prompt="固定規則",
                max_tokens=1024,
            )

        self.assertEqual(result, 0)
        self.assertIn("Day 7 checkpoint：PASS", stdout.getvalue())
        self.assertEqual(call.call_count, 2)
        self.assertTrue(call.call_args_list[0].kwargs["json_answer"])
        self.assertEqual(call.call_args_list[0].kwargs["temperature"], 0)
        self.assertEqual(call.call_args_list[0].kwargs["history"], [])
        self.assertEqual(
            call.call_args_list[1].kwargs["history"],
            [
                {"role": "user", "content": runner.CHECKPOINT_FIRST_PROMPT},
                {"role": "assistant", "content": first},
            ],
        )

    def test_checkpoint_fails_when_history_answer_is_wrong(self):
        answers = [
            json.dumps({"answer": "收到", "limitations": []}),
            json.dumps({"answer": "不知道", "limitations": ["缺少上下文"]}),
        ]

        with patch.object(
            runner, "call_local_model", side_effect=answers
        ), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
            io.StringIO()
        ) as stderr:
            result = runner.run_checkpoint(
                base_url="test",
                model=None,
                system_prompt="固定規則",
                max_tokens=1024,
            )

        self.assertEqual(result, 1)
        self.assertIn("沒有按約定回答第一輪的代號", stderr.getvalue())

    def test_checkpoint_fails_when_first_answer_ignores_contract(self):
        first = json.dumps({"answer": "好的", "limitations": []}, ensure_ascii=False)

        with patch.object(
            runner, "call_local_model", return_value=first
        ), contextlib.redirect_stderr(io.StringIO()) as stderr:
            result = runner.run_checkpoint(
                base_url="test",
                model=None,
                system_prompt="固定規則",
                max_tokens=1024,
            )

        self.assertEqual(result, 1)
        self.assertIn("第一輪沒有按約定回答", stderr.getvalue())

    def test_checkpoint_reports_runtime_failure(self):
        with patch.object(
            runner, "call_local_model", side_effect=RuntimeError("連線失敗")
        ), contextlib.redirect_stderr(io.StringIO()) as stderr:
            result = runner.run_checkpoint(
                base_url="test",
                model=None,
                system_prompt="固定規則",
                max_tokens=1024,
            )

        self.assertEqual(result, 1)
        self.assertIn("連線失敗", stderr.getvalue())

    def test_cli_rejects_checkpoint_mode_conflicts(self):
        cases = [
            ["runner", "--checkpoint", "問題"],
            ["runner", "--checkpoint", "--interactive"],
            ["runner", "--checkpoint", "--no-system-prompt"],
            ["runner", "--checkpoint", "--json-answer"],
            ["runner", "--checkpoint", "--no-history"],
        ]

        for argv in cases:
            with self.subTest(argv=argv), patch("sys.argv", argv), contextlib.redirect_stderr(
                io.StringIO()
            ), self.assertRaises(SystemExit) as error:
                runner.parse_args()
            self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
