# source-to-raw-md

A Codex skill and CLI that converts complete text files, text-layer PDFs, and static web pages into source-linked Markdown without an LLM. It preserves originals in `knowledge/inbox/` and writes fixed-format Markdown to `knowledge/raw/`.

In the AI Engineering Frontier project, readers run the batch entrypoint directly from the terminal. Put files in `knowledge/inbox/`, then run:

```bash
uv run --with pypdf --with fonttools python knowledge/convert.py
```

It processes supported files, verifies each raw result, and moves successful originals to `knowledge/inbox/processed/`. It skips that folder on later runs. Failed and unsupported files stay in the pending `inbox/` area. This Day 8 command does not require Qwen or a model tool-calling interface. `knowledge/convert.py` is a thin project entrypoint to this skill's `scripts/batch.py`.

Day 17's `import_web_source` tool calls `batch.convert_selected_source()` after the user selects a search result. It processes only that pending snapshot, preserves its `.source.json` provenance sidecar, writes and validates the corresponding raw Markdown, then the caller rebuilds the manifest and FTS5 index. The sidecar records the source URL, display title, and charset without modifying the downloaded page bytes.

## Requirements

- Python 3.13+
- `pypdf` for PDF input (`fonttools` can help with some embedded fonts)

For a different project, create `knowledge/inbox/` there and run the standalone batch command:

```bash
uv run --with pypdf --with fonttools python /path/to/source-to-raw-md/scripts/batch.py --project-root /path/to/project
```

For a single source outside that project:

```bash
uv run --with pypdf --with fonttools python /path/to/source-to-raw-md/scripts/convert.py notes.txt
uv run --with pypdf --with fonttools python /path/to/source-to-raw-md/scripts/convert.py report.pdf
uv run --with pypdf --with fonttools python /path/to/source-to-raw-md/scripts/convert.py https://example.com
```

Set `--source-dir` and `--output-dir` to choose storage paths. The script processes every PDF page and never truncates extracted text to fit a model context. It refuses a PDF if any page has no extractable text. The 100 MiB file cap is a safety limit, independent of context length.

For PDFs, output covers the extracted text layer, with page boundaries and source hashes. Figures, tables, equations, and multi-column order still need comparison with the original PDF. Scans need OCR before this converter can handle them. Static HTML may include navigation; iT 邦幫忙 articles use a specific article-body selector. JavaScript-only page content is unsupported.

Document IDs use the local file name and bytes, or a web URL and selected article text. For unchanged web article text, navigation or ad changes do not create a new ID. Existing output with the same ID and converter version is reused; an incompatible old output is preserved and reported as a conflict.

The Day 8 raw format is a Markdown file named `<document_id>.md`, with JSON-encoded YAML frontmatter values followed by the full converted body. Required fields are `document_id`, `source_name`, `source_type`, `source_format`, `source_sha256`, `source_snapshot`, `extracted_sha256`, `conversion_method`, and `converter_version`. PDFs also include `pdf_pages` and `extraction_scope`; downloaded sources include `source_url`.

Validate a directory against its saved originals:

```bash
uv run --with pypdf --with fonttools python /path/to/source-to-raw-md/scripts/validate.py knowledge/raw
```

The checker recomputes source hashes, Document IDs, extraction, and body text. It verifies this format and the converter's output, not the fidelity of charts or a later ingest pipeline.

See [SKILL.md](SKILL.md) for agent instructions. The code is MIT licensed and uses only Python's standard library plus `pypdf` for PDF extraction.
