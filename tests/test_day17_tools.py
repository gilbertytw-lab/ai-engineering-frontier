import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).parents[1]
SCRIPT = PROJECT_ROOT / "knowledge" / "tools.py"
spec = importlib.util.spec_from_file_location("day17_tools", SCRIPT)
tools = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = tools
spec.loader.exec_module(tools)
web_sources = sys.modules["web_sources"]


def completion(message, finish_reason="stop"):
    return {
        "choices": [{"finish_reason": finish_reason, "message": message}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5},
    }


def function_call(name, arguments, call_id="call-1"):
    return {
        "id": call_id,
        "type": "function",
        "function": {"name": name, "arguments": arguments},
    }


def public_dns(host, port, type):
    return [(None, None, None, None, ("93.184.216.34", port))]


class Day17WebSearchTests(unittest.TestCase):
    def test_parse_search_results_extracts_redirect_url_and_snippet(self):
        page = """
        <div class="result">
          <a class="result__a" href="/l/?uddg=https%3A%2F%2Fexample.com%2Ffts">SQLite FTS5</a>
          <div class="result__snippet">Official <b>SQLite</b> documentation.</div>
        </div>
        <div class="result">
          <a class="result__a" href="http://127.0.0.1/private">Internal page</a>
          <div class="result__snippet">Must be filtered.</div>
        </div>
        """
        with patch.object(web_sources.socket, "getaddrinfo", side_effect=public_dns):
            results = web_sources.parse_search_results(page)

        self.assertEqual(
            results,
            [
                {
                    "title": "SQLite FTS5",
                    "url": "https://example.com/fts",
                    "snippet": "Official SQLite documentation.",
                }
            ],
        )

    def test_web_search_saves_bounded_candidates_for_later_selection(self):
        html = b"""
        <div class="result">
          <a class="result__a" href="https://example.com/fts">SQLite FTS5</a>
          <div class="result__snippet">Official documentation.</div>
        </div>
        """

        def fake_fetcher(url, *, max_bytes, allowed_types):
            self.assertIn("duckduckgo.com/lite/", url)
            self.assertEqual(max_bytes, web_sources.MAX_SEARCH_BYTES)
            self.assertEqual(allowed_types, {"text/html"})
            return html, url, "text/html", "utf-8"

        with tempfile.TemporaryDirectory() as directory, patch.object(
            web_sources.socket, "getaddrinfo", side_effect=public_dns
        ):
            results_path = Path(directory) / "results.json"
            result = web_sources.web_search(
                query=" SQLite FTS5 ", results_path=results_path, fetcher=fake_fetcher
            )
            saved = json.loads(results_path.read_text(encoding="utf-8"))

        self.assertEqual(result["query"], "SQLite FTS5")
        self.assertEqual(result["result_count"], 1)
        self.assertEqual(result["results"][0]["source_id"], "web-1")
        self.assertEqual(saved["results"][0]["url"], "https://example.com/fts")

    def test_search_rejects_empty_and_oversized_queries(self):
        for query in ("  ", "q" * (tools.MAX_WEB_QUERY_LENGTH + 1)):
            with self.subTest(query_length=len(query)), self.assertRaises(tools.ToolCallError):
                tools.parse_tool_arguments(json.dumps({"query": query}), tool_name="web_search")

        with self.assertRaises(tools.ToolCallError):
            tools.parse_tool_arguments(
                '{"query":"sqlite","limit":99}', tool_name="web_search"
            )

    def test_failed_search_invalidates_candidates_from_an_older_query(self):
        with tempfile.TemporaryDirectory() as directory:
            results_path = Path(directory) / "results.json"
            results_path.write_text(
                json.dumps({"version": 1, "results": [{"source_id": "web-1"}]}),
                encoding="utf-8",
            )

            def failed_fetcher(url, **kwargs):
                raise web_sources.WebSearchError("provider unavailable")

            with self.assertRaises(web_sources.WebSearchError):
                web_sources.web_search(
                    query="new query", results_path=results_path, fetcher=failed_fetcher
                )
            saved = json.loads(results_path.read_text(encoding="utf-8"))

        self.assertEqual(saved["query"], "new query")
        self.assertEqual(saved["results"], [])

    def test_import_saves_original_and_uses_existing_converter(self):
        page = b"<html><head><title>SQLite FTS5</title></head><body><article><h1>SQLite FTS5</h1><p>FTS5 provides full-text search.</p></article></body></html>"
        with tempfile.TemporaryDirectory() as directory, patch.object(
            web_sources.socket, "getaddrinfo", side_effect=public_dns
        ):
            root = Path(directory)
            results_path = root / "runs" / "search.json"
            results_path.parent.mkdir(parents=True)
            results_path.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "results": [
                            {
                                "source_id": "web-1",
                                "title": "SQLite FTS5",
                                "url": "https://example.com/fts",
                                "snippet": "Official documentation.",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            def fake_fetcher(url, *, max_bytes, allowed_types):
                self.assertEqual(url, "https://example.com/fts")
                self.assertEqual(allowed_types, {"text/html", "application/xhtml+xml", "text/plain", "application/pdf"})
                return page, url, "text/html", "utf-8"

            result = web_sources.save_and_convert_web_source(
                source_id="web-1",
                results_path=results_path,
                inbox=root / "knowledge" / "inbox",
                raw=root / "knowledge" / "raw",
                root=root,
                fetcher=fake_fetcher,
            )
            raw_path = Path(result["raw_path"])
            raw_text = raw_path.read_text(encoding="utf-8")
            snapshot = Path(result["inbox_path"])
            if not snapshot.is_absolute():
                snapshot = root / snapshot
            self.assertEqual(result["status"], "converted")
            self.assertTrue(raw_path.is_file())
            self.assertTrue(snapshot.is_file())
            self.assertIn('source_url: "https://example.com/fts"', raw_text)
            self.assertIn("FTS5 provides full-text search.", raw_text)
            self.assertFalse((root / "knowledge" / "inbox" / snapshot.name).exists())

    def test_import_refuses_unselected_or_unknown_source(self):
        importer_calls = []
        call = function_call("import_web_source", '{"source_id":"web-1"}')
        self.assertTrue(tools._has_explicit_selection("我選web-2，請匯入", "web-2"))
        self.assertFalse(tools._has_explicit_selection("我選web-20，請匯入", "web-2"))
        self.assertFalse(tools._has_explicit_selection("xweb-2，請匯入", "web-2"))
        self.assertFalse(tools._has_explicit_selection("我不選web-2，請匯入", "web-2"))
        self.assertFalse(tools._has_explicit_selection("我選web-2，但請勿匯入", "web-2"))
        with self.assertRaises(tools.ToolCallError):
            tools.execute_tool_call(
                call,
                user_question="請說明 web-1 的摘要",
                import_source_fn=lambda **kwargs: importer_calls.append(kwargs),
            )
        self.assertEqual(importer_calls, [])

        with tempfile.TemporaryDirectory() as directory:
            results_path = Path(directory) / "missing.json"
            with self.assertRaises(web_sources.WebSearchError):
                web_sources.save_and_convert_web_source(
                    source_id="web-1", results_path=results_path
                )

        with self.assertRaises(tools.ToolCallError):
            tools.execute_tool_call(
                call,
                user_question="我選 web-1，但不匯入。",
                import_source_fn=lambda **kwargs: importer_calls.append(kwargs),
            )
        self.assertEqual(importer_calls, [])

    def test_explicit_selection_imports_and_rebuilds_index(self):
        imported = []
        rebuilt = []

        def fake_importer(**kwargs):
            imported.append(kwargs)
            return {"status": "converted", "raw_path": "knowledge/raw/doc.md"}

        def fake_rebuild(*, root):
            rebuilt.append(root)
            return {"document_count": 6, "chunk_count": 15}

        call = function_call("import_web_source", '{"source_id":"web-2"}')
        _, result = tools.execute_tool_call(
            call,
            user_question="我選第 2 筆，請匯入知識庫。",
            root=Path("/tmp/day17-fixture"),
            import_source_fn=fake_importer,
            index_rebuilder=fake_rebuild,
        )

        self.assertEqual(len(imported), 1)
        self.assertEqual(imported[0]["source_id"], "web-2")
        self.assertEqual(rebuilt, [Path("/tmp/day17-fixture")])
        self.assertEqual(result["index_status"], "updated")
        self.assertEqual(result["index"]["chunk_count"], 15)

    def test_tool_turn_returns_candidates_without_importing_them(self):
        calls = []

        def fake_completion(messages, **kwargs):
            calls.append((messages, kwargs))
            if len(calls) == 1:
                return completion(
                    {
                        "role": "assistant",
                        "content": None,
                        "tool_calls": [
                            function_call("web_search", '{"query":"SQLite FTS5 官方文件"}')
                        ],
                    },
                    finish_reason="tool_calls",
                )
            return completion(
                {
                    "role": "assistant",
                    "content": "找到 web-1：SQLite FTS5。要匯入請告訴我選哪一筆。",
                }
            )

        record = tools.run_tool_turn(
            "本地文件沒有 FTS5 說明，請上網搜尋。",
            web_search_fn=lambda *, query, results_path: {
                "query": query,
                "result_count": 1,
                "results": [
                    {
                        "source_id": "web-1",
                        "title": "SQLite FTS5",
                        "url": "https://www.sqlite.org/fts5.html",
                        "snippet": "Official documentation.",
                    }
                ],
            },
            completion_fn=fake_completion,
        )

        self.assertEqual(record["tool_name"], "web_search")
        self.assertEqual(record["tool_result"]["result_count"], 1)
        self.assertEqual(record["model_calls"], 2)
        self.assertNotIn("import_web_source", record["tool_result"])

    def test_schemas_expose_search_and_import_not_config_check(self):
        captured = []

        def fake_completion(messages, **kwargs):
            captured.append(kwargs)
            return completion({"role": "assistant", "content": "完成。"})

        tools.run_tool_turn("直接回答", completion_fn=fake_completion)
        names = {item["function"]["name"] for item in captured[0]["tools"]}
        self.assertEqual(
            names,
            {"list_sources", "get_document_chunks", "web_search", "import_web_source"},
        )


if __name__ == "__main__":
    unittest.main()
