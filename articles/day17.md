# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 17：知識庫找不到答案時，讓使用者挑來源再匯入

Day 16 的 `get_document_chunks` 最多能從指定文件取回 3 個片段。Day 17 把查找範圍接到網頁：本地資料不足時，`web_search` 先列出候選；使用者選定來源後，`import_web_source` 才下載、轉換並更新索引。搜尋和匯入分兩回合，第一回合不會直接寫入知識庫。

```text
本地來源查找
    ↓ 找不到足夠證據
web_search：回傳候選標題、網址、摘要
    ↓ 使用者選定來源 ID
import_web_source：保存原件 → 轉成 raw → 重建索引
```

## 搜尋只負責列候選

`web_search` 的 `query` 最長 300 個字元，使用 DuckDuckGo Lite 搜尋，最多回傳 5 筆。每筆結果都有標題、網址、摘要和 `web-1` 到 `web-5` 的來源 ID。ID 會存進 Git 忽略的 `runs/day17-web-search.json`，供下一輪辨認使用者選了哪筆。

搜尋摘要只供使用者判斷，不會寫進 `raw/`。使用者要匯入時，須在下一回合指定來源 ID，例如「我選第 2 筆，請匯入」。分派器會比對 ID 和這一回合的使用者訊息；模型只能傳來源 ID，網址則由程式從最近一次搜尋紀錄查出。模型不能自行指定網址或檔案路徑。

```json
{
  "name": "import_web_source",
  "parameters": {
    "type": "object",
    "properties": {
      "source_id": {
        "type": "string",
        "pattern": "^web-[1-5]$"
      }
    },
    "required": ["source_id"],
    "additionalProperties": false
  }
}
```

Python 會先檢查網址，只接受 HTTP 或 HTTPS；如果網址解析到本機或內部 IP，便拒絕下載。每份來源最多 20 MiB，格式限於靜態 HTML、文字和 PDF。模型多傳 `path` 或其他參數也不會改變這些限制。

## 網頁交給既有轉換器處理

使用者選定來源後，`import_web_source` 才會下載內容。原始位元組存入 `knowledge/inbox/`；另一份 `.source.json` 記錄來源網址、搜尋標題和字元編碼，原始檔保持不變。

接著，程式呼叫 `source-to-raw-md` 的 `batch.convert_selected_source()`，只處理剛選定的檔案。驗證通過後，原件和中繼資料移到 `knowledge/inbox/processed/`，轉換後的 Markdown 寫入 `knowledge/raw/`。Markdown 的 `source_snapshot` 和 `source_url` 欄位可用來查看保存的來源檔案並追查來源網址。

轉換成功後，程式沿用 manifest 的 tokenizer 和 chunk 設定，重建 chunk manifest 與 SQLite FTS5 索引；新文件即可參與本地查找，不必另外執行索引命令。如果正文由 JavaScript 載入，或 PDF 沒有可抽取的文字，轉換器會回報失敗，來源則留在待處理區供人檢查。

## 跑一次搜尋，再決定是否匯入

先啟動本地模型服務。搜尋網頁需要網路連線；本地模型仍透過原本的 MLX-LM endpoint 回答。

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

在另一個終端機先問本地資料不足的問題：

```bash
uv run python knowledge/tools.py \
  "本地文件沒有說明 FTS5 的限制，請上網找官方資料。"
```

模型會呼叫 `web_search`，再列出候選來源。使用者看過標題和網址後，才在下一個回合指定要匯入的來源：

```bash
uv run python knowledge/tools.py \
  "我選 web-1，請把這筆來源匯入知識庫。"
```

第二輪會從 `runs/day17-web-search.json` 讀取最近一次搜尋結果，模型再呼叫 `import_web_source`。每一回合仍最多執行一個工具，所以模型無法在第一次搜尋時跳過使用者選擇、直接把候選寫入知識庫。

## 實際轉換與檢索結果

我用 `SQLite FTS5 official documentation` 查詢 DuckDuckGo Lite，取得 5 筆候選，並在暫存目錄選取第一筆 [SQLite 官方的 FTS5 文件](https://sqlite.org/fts5.html) `web-1`。程式完成擷取、轉成 raw Markdown 與索引重建，輸出都留在暫存目錄，沒有寫入專案知識庫。

頁面轉成 raw Markdown 後共 170,494 bytes，分成 334 個 chunks。`SQLite FTS5` 查詢回傳該來源的 3 個 chunks。搜尋、擷取、來源欄位、原件保存和索引重建都用真實網頁檢查；工具回合則以模擬模型回應測試。

Day 17 的 9 個工具測試、Day 16 的 7 個工具測試與全專案 76 個測試都通過。

啟動 `mlx-community/Qwen3.8-27B-4bit` 後，我也跑了 `knowledge/tools.py --checkpoint`。四個模型案例全數通過：兩個知識庫查詢、一個不需工具的算術題，以及 `web_search` 工具選擇。checkpoint 的搜尋候選使用固定 fixture；這裡驗證的是 Qwen 是否會選工具並整理工具結果，不是即時搜尋。

即時搜尋另用暫存候選記錄驗證，避免舊的候選影響新回合。Qwen 的即時搜尋回合也使用 `web_search`，取得 5 筆候選，並將 SQLite 官方 FTS5 文件列為第一筆。兩次模型呼叫和一次工具呼叫後，Qwen 請使用者選定來源；這次停在候選階段，沒有匯入。整回合耗時 103,670.7 ms。

網頁摘要和正文都視為不可信資料。`system prompt` 會提醒模型不要遵循其中要求忽略規則的文字，但這只是行為提醒。頁面內容不會被當成要執行的指令；實際可匯入的來源仍由來源 ID、網址檢查和 Python 分派器限制。

## 參考資料

- [SQLite FTS5 官方文件](https://sqlite.org/fts5.html)
- [專案程式碼](https://github.com/gilbertytw-lab/ai-engineering-frontier)
