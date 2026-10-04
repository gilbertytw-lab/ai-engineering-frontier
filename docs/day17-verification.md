# Day 17 驗證紀錄

驗證日期：2026-10-01（Asia/Taipei）。本日將 Day 17 從 Harbor 範例設定檢查改為使用者選定的網頁來源匯入流程。

文章：[Day 17：本地找不到時，讓使用者挑選網頁來源再匯入](../articles/day17.md)

## 實作範圍

- `web_search` 使用 DuckDuckGo Lite，最多回傳 5 筆標題、網址與摘要，並將最近一次候選 ID 保存在 Git 忽略的 `runs/day17-web-search.json`。
- 搜尋本身不下載候選來源，也不寫入知識庫。新搜尋開始時會清除舊候選；搜尋失敗時不能拿前一次結果誤匯入。
- `import_web_source` 只接受最近一次搜尋結果中的 `web-1` 到 `web-5`，且 Python 會檢查目前使用者訊息有明確選取／匯入指示。
- 擷取只接受 HTTP/HTTPS，拒絕本機或內部 IP，限制來源大小 20 MiB，並只處理靜態 HTML、文字或 PDF。
- 原始來源位元組存入 `knowledge/inbox/`，來源網址、搜尋標題和編碼放在 `.source.json` sidecar。既有 `source-to-raw-md` batch converter 只處理該來源，驗證成功後將原件移入 `inbox/processed/`，raw frontmatter 保存來源網址與快照路徑。
- 轉換成功後，以 manifest 現有 tokenizer 和 chunk 設定重建 manifest 與 SQLite FTS5 索引。
- 網頁標題、摘要與正文均視為不可信資料；不提供任意 URL、檔案路徑或一般檔案寫入工具。

## 自動化測試

```bash
uv run python -m unittest tests.test_day17_tools tests.test_day16_tools -v
uv run python -m unittest discover -s tests -v
uv run python -m py_compile knowledge/tools.py knowledge/web_sources.py skills/source-to-raw-md/scripts/batch.py skills/source-to-raw-md/scripts/convert.py
git diff --check
```

Day 17 的 9 個測試和 Day 16 的 7 個測試通過；全專案 76 個測試通過。測試涵蓋搜尋結果解析、查詢限制、失敗時清除舊候選、未明確選取時拒絕匯入、只匯入所選來源、保存 provenance sidecar、轉換到 raw、索引重建呼叫，以及工具結果回傳模型。

## 實際網路與轉換驗證

以「SQLite FTS5 official documentation」查詢 DuckDuckGo Lite，取得 5 筆候選。驗證程式在系統暫存目錄中選取官方 SQLite FTS5 文件，完成網頁擷取、保存來源快照、轉換、`validate_file` 驗證與索引重建。暫存資料沒有寫入 Repository 的 `knowledge/`。

```text
search_results=5
selected=web-1
document_count=1
chunk_count=334
retrieved_source=SQLite FTS5 Extension
retrieved_chunks=3
```

轉出的 raw Markdown 為 170,494 bytes，並保留原始網址與快照路徑。FTS5 查詢 `SQLite FTS5` 找回這份來源的 3 個 chunks。

## Qwen checkpoint 與限制

啟動本機服務後，重新執行 Day 17 checkpoint，四個 Qwen 案例全數通過：`list_sources`、`get_document_chunks`、`web_search`，以及不需工具時直接回答。checkpoint 的搜尋候選使用固定 fixture，只驗證模型是否會選對工具並整理工具結果。

接著以暫存檔作為搜尋結果記錄，讓 Qwen 走一次即時 DuckDuckGo Lite 搜尋。完整回合結果：

```text
model_calls=2
tool_call_count=1
tool=web_search
query=SQLite FTS5 official documentation
result_count=5
recommended=web-1 (SQLite FTS5 Extension, https://sqlite.org/fts5.html)
imported=false
elapsed_ms=103670.7
```

Qwen 列出五筆候選，將 SQLite 官方 FTS5 文件排在第一筆，並要求使用者明確選取後才匯入。此回合沒有選取來源，因此沒有執行匯入，也沒有寫入知識庫。暫存 `results_path` 同時避免先前失敗回合留下的候選影響本次選擇。

第一次即時搜尋已成功取得候選，但 Qwen 在整理五筆結果時撞上原本 256-token 的最終回覆上限，回傳 `finish_reason=length`。因此把工具結果後的回覆上限提高到 768 tokens，再跑即時回合後正常完成。checkpoint 的查詢檢查也改為確認 query 含 `sqlite` 與 `fts5`，不要求模型逐字採用中文提示；Qwen 實際送出的搜尋詞是英文。

本次另重新執行全專案測試：76 個測試通過。真實網頁擷取、轉換和索引重建仍依前述暫存目錄驗證，Qwen 即時搜尋回合則停在候選階段，沒有匯入。

DuckDuckGo Lite 的 HTML 結構屬外部服務介面，服務可能改版或要求人工驗證；遇到驗證頁時工具會回報搜尋失敗，不會使用舊結果。JavaScript-only 網頁、沒有文字層的 PDF 和超過 20 MiB 的來源不會自動轉換。若 converter 成功但 tokenizer 載入或索引重建失敗，raw 和原始快照仍會保留，工具結果會回報 `index_status=failed`。

## 風格配方紀錄

教學實作型｜Simon 實證筆記風味｜標準｜單稿。文章以可重現流程、實際搜尋結果、轉換 bytes/chunks 和支援邊界作為證據；沒有加入未發生的個人經歷。

`speak-human-tw` detect-first 語感檢查：0 處需提出改寫。保留工具限制、驗證數字與直接說明匯入控制邊界的句子；另將來源快照描述改成「來源檔案」，以涵蓋 HTML、文字與 PDF。

`humanizer-zh` 未安裝於目前環境，因此沒有執行 blog-writing-zh 要求的下游檢查。可接續使用這段指令：「請用 humanizer-zh 以 detect 模式、technical voice 檢查 `articles/day17.md`，只列 AI 寫作痕跡，不要改字；保留技術限制、實測數字、來源和刻意的技術判斷句。」
