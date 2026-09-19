import contextlib
import io
import json
import unittest
from unittest.mock import patch

import frontier_knowledge as runner


class AnswerTests(unittest.TestCase):
    def test_valid_answers(self):
        for limits in ([], ["未提供測試紀錄"]):
            value = {"answer": "不知道", "limitations": limits}
            self.assertEqual(runner.parse_answer(json.dumps(value)), value)

    def test_rejects_invalid_answers(self):
        cases = [
            'hello', '```json\n{"answer":"ok","limitations":[]}\n```',
            '{"answer":', '[]', 'null', '{}',
            '{"answer":"ok","limitations":[],"extra":1}',
            '{"answer":null,"limitations":[]}',
            '{"answer":"  ","limitations":[]}',
            '{"answer":3,"limitations":[]}',
            '{"answer":"ok","limitations":"none"}',
            '{"answer":"ok","limitations":[1]}',
            '{"answer":"ok","limitations":[" "]}',
            '{"answer":"a","answer":"b","limitations":[]}',
            '{"answer":"ok","limitations":[NaN]}',
            '{"answer":"ok","limitations":[]} trailing',
        ]
        for content in cases:
            with self.subTest(content=content), self.assertRaises(RuntimeError):
                runner.parse_answer(content)

    def invoke(self, content, structured=True):
        response = io.BytesIO(json.dumps({"choices": [{"message": {"content": content}}]}).encode())
        with patch.object(runner, "urlopen", return_value=response) as request:
            result = runner.call_local_model(
                "問題", base_url="http://localhost:8081/v1", model="test-model",
                system_prompt="原本規則", temperature=0.2, max_tokens=1024,
                json_answer=structured,
            )
            payload = json.loads(request.call_args.args[0].data)
        return result, payload

    def test_payload_and_roundtrip(self):
        answer = {"answer": "不知道", "limitations": []}
        result, payload = self.invoke(json.dumps(answer))
        self.assertEqual(json.loads(result), answer)
        self.assertEqual(payload["messages"][0]["content"], "原本規則\n" + runner.JSON_ANSWER_PROMPT)
        self.assertEqual(payload["messages"][1], {"role": "user", "content": "問題"})
        self.assertNotIn("response_format", payload)

    def test_text_mode_unchanged(self):
        result, payload = self.invoke("一般回答", False)
        self.assertEqual(result, "一般回答")
        self.assertEqual(payload["messages"][0]["content"], "原本規則")
        self.assertEqual(runner.build_messages("問題", None), [{"role": "user", "content": "問題"}])

    def test_invalid_content_not_accepted(self):
        for content in (None, "", "  ", {}, "普通文字"):
            with self.subTest(content=content), self.assertRaises(RuntimeError):
                self.invoke(content)

    def test_cli_rejects_conflicting_flags(self):
        with patch("sys.argv", ["runner", "--json-answer", "--no-system-prompt", "問題"]):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                runner.parse_args()
        self.assertEqual(error.exception.code, 2)

    def test_single_failure_exit(self):
        with patch("sys.argv", ["runner", "--json-answer", "問題"]), patch.object(
            runner, "call_local_model", side_effect=RuntimeError("格式錯誤")
        ), contextlib.redirect_stderr(io.StringIO()) as stderr, contextlib.redirect_stdout(io.StringIO()) as stdout:
            self.assertEqual(runner.main(), 1)
        self.assertIn("格式錯誤", stderr.getvalue())
        self.assertEqual(stdout.getvalue(), "")

    def test_interactive_continues_after_failure(self):
        with patch("builtins.input", side_effect=["第一題", "第二題", "exit"]), patch.object(
            runner, "call_local_model", side_effect=[RuntimeError("格式錯誤"), '{"answer":"ok","limitations":[]}']
        ) as call, contextlib.redirect_stdout(io.StringIO()) as stdout, contextlib.redirect_stderr(io.StringIO()) as stderr:
            result = runner.run_interactive(base_url="test", model=None, system_prompt="規則", temperature=0.2, max_tokens=1024, json_answer=True)
        self.assertEqual(result, 0)
        self.assertEqual(call.call_count, 2)
        self.assertTrue(all(c.kwargs["json_answer"] for c in call.call_args_list))
        self.assertIn('"answer":"ok"', stdout.getvalue())
        self.assertIn("格式錯誤", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
