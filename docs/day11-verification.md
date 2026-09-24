# Day 11 驗證紀錄

## 範圍

Day 11 新增 `knowledge/wiki.py`，從 `knowledge/raw/*.md` 自動建立來源導覽層：

- `knowledge/wiki/index.md`
- `knowledge/wiki/sources/*.md`

每個 source page 保留 `document_id`、來源檔名、raw 路徑、source snapshot、hash 和 converter 資訊。頁面不複製 raw 正文，也不需要使用者手動替文件分類。

本日沒有啟動 Qwen，也沒有把 wiki 接進 FTS5 或 Chat Runner。這一版只驗證來源頁的產生、回查和重建行為。

## 實際命令

```bash
uv run python knowledge/wiki.py
```

輸出：

```text
建立 /Users/gilbert/Projects/ai-engineering-frontier/knowledge/wiki：5 份來源、5 個 source pages、index.md
```

產物：

- 1 個 `index.md`
- 5 個 source pages
- 每頁都連回 `knowledge/raw/` 的對應文件

## 自動化測試

```bash
uv run python -m unittest tests.test_day11_wiki -v
```

結果：Day 11 測試 3 項通過。

測試涵蓋：

- 相同 raw 輸入重跑後，所有 wiki 文件內容完全相同。
- source page 保留 provenance 和 raw 連結。
- 過期的 generated source page 會移除，手寫頁面會保留。
- 重複 `document_id` 會被拒絕。

完整回歸：

```bash
uv run python -m unittest discover -s tests -v
```

結果：35 項測試全數通過。

## 已知限制

- 目前只產生 `source` 頁，不產生 `concept`、`howto` 或 `derived` 頁。
- source catalog 尚未接入 FTS5 檢索流程。
- wiki 頁面沒有複製 raw 正文，完整證據仍要回到 `knowledge/raw/`。
- 產生器只接受帶有既定 frontmatter 的 raw Markdown。
