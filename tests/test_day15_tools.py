import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "knowledge" / "tools.py"
spec = importlib.util.spec_from_file_location("day15_tools", SCRIPT)
tools = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = tools
spec.loader.exec_module(tools)


def completion(message, finish_reason="stop"):
    return {
        "choices": [{"finish_reason": finish_reason, "message": message}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5},
    }


def function_call(name="list_sources", arguments='{"name_contains":"deploy"}', call_id="call-1"):
    return {
        "id": call_id,
        "type": "function",
        "function": {"name": name, "arguments": arguments},
    }


class Day15ToolTests(unittest.TestCase):
    def manifest(self, directory):
        path = Path(directory) / "manifest.json"
        path.write_text(
            json.dumps(
                {
                    "documents": [
                        {"source_name": "deployment-guide.md", "document_id": "doc-deploy"},
                        {"source_name": "service-config.md", "document_id": "doc-config"},
                    ]
                }
            ),
            encoding="utf-8",
        )
        return path

    def test_list_sources_returns_only_allowlisted_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            result = tools.list_sources(
                name_contains="DEPLOY", manifest_path=self.manifest(directory)
            )

        self.assertEqual(
            result,
            {"sources": [{"source_name": "deployment-guide.md", "document_id": "doc-deploy"}]},
        )
        self.assertEqual(set(result["sources"][0]), {"source_name", "document_id"})

    def test_only_allowlisted_function_can_execute(self):
        with self.assertRaisesRegex(tools.ToolCallError, "允許清單"):
            tools.execute_tool_call(function_call(name="delete_source"))
        malformed_name = function_call()
        malformed_name["function"]["name"] = ["list_sources"]
        with self.assertRaisesRegex(tools.ToolCallError, "允許清單"):
            tools.execute_tool_call(malformed_name)

    def test_path_and_extra_arguments_are_rejected(self):
        with self.assertRaisesRegex(tools.ToolCallError, "只接受 name_contains"):
            tools.execute_tool_call(
                function_call(arguments='{"name_contains":"deploy","path":"/tmp/secret"}')
            )

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaisesRegex(tools.ToolCallError, "重複欄位"):
            tools.parse_tool_arguments('{"name_contains":"deploy","name_contains":""}')

    def test_invalid_types_and_oversized_filters_are_rejected(self):
        with self.assertRaisesRegex(tools.ToolCallError, "必須是字串"):
            tools.parse_tool_arguments('{"name_contains":4}')
        with self.assertRaisesRegex(tools.ToolCallError, "不可超過"):
            tools.parse_tool_arguments(json.dumps({"name_contains": "x" * 81}))

    def test_model_without_tool_call_uses_one_completion(self):
        calls = []

        def fake_completion(messages, **kwargs):
            calls.append((messages, kwargs))
            return completion({"role": "assistant", "content": "4"})

        record = tools.run_tool_turn("2 加 2 等於多少？", completion_fn=fake_completion)

        self.assertEqual(record["answer"], "4")
        self.assertEqual(record["tool_call_count"], 0)
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][1]["tools"], tools.TOOL_SCHEMAS)

    def test_model_tool_call_executes_once_then_returns_result_for_final_answer(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest_path = self.manifest(directory)

            calls = []

            def fake_completion(messages, **kwargs):
                calls.append((messages, kwargs))
                if len(calls) == 1:
                    return completion(
                        {"role": "assistant", "content": None, "tool_calls": [function_call()]},
                        finish_reason="tool_calls",
                    )
                return completion({"role": "assistant", "content": "deployment-guide.md"})

            record = tools.run_tool_turn(
                "列出 deployment 來源",
                manifest_path=manifest_path,
                completion_fn=fake_completion,
            )

        self.assertEqual(record["tool_name"], "list_sources")
        self.assertEqual(record["tool_result"]["sources"][0]["source_name"], "deployment-guide.md")
        self.assertEqual(record["answer"], "deployment-guide.md")
        self.assertEqual(record["model_calls"], 2)
        self.assertEqual(calls[1][0][-1]["role"], "tool")
        self.assertNotIn("tools", calls[1][1])

    def test_multiple_calls_are_rejected_before_any_tool_runs(self):
        completion_fn = lambda *args, **kwargs: completion(
            {
                "role": "assistant",
                "content": None,
                "tool_calls": [function_call(), function_call(call_id="call-2")],
            },
            finish_reason="tool_calls",
        )
        with patch.object(tools, "list_sources", side_effect=AssertionError("must not execute")):
            with self.assertRaisesRegex(tools.ToolCallError, "最多允許 1 個"):
                tools.run_tool_turn("列出來源", completion_fn=completion_fn)

    def test_non_list_tool_calls_are_rejected(self):
        completion_fn = lambda *args, **kwargs: completion(
            {"role": "assistant", "content": None, "tool_calls": {"unexpected": "object"}},
            finish_reason="tool_calls",
        )
        with self.assertRaisesRegex(tools.ToolCallError, "必須是陣列"):
            tools.run_tool_turn("列出來源", completion_fn=completion_fn)

    def test_invalid_call_arguments_never_reach_the_tool(self):
        completion_fn = lambda *args, **kwargs: completion(
            {
                "role": "assistant",
                "content": None,
                "tool_calls": [function_call(arguments='{"name_contains":"deploy","path":"/tmp"}')],
            },
            finish_reason="tool_calls",
        )
        with patch.object(tools, "list_sources", side_effect=AssertionError("must not execute")):
            with self.assertRaisesRegex(tools.ToolCallError, "只接受 name_contains"):
                tools.run_tool_turn("列出來源", completion_fn=completion_fn)

    def test_second_model_tool_request_is_rejected(self):
        calls = 0

        def fake_completion(messages, **kwargs):
            nonlocal calls
            calls += 1
            return completion(
                {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [function_call(call_id=f"call-{calls}")],
                },
                finish_reason="tool_calls",
            )

        with self.assertRaisesRegex(tools.ToolCallError, "只允許執行一次工具"):
            tools.run_tool_turn("列出 deployment 來源", completion_fn=fake_completion)
        self.assertEqual(calls, 2)


if __name__ == "__main__":
    unittest.main()
