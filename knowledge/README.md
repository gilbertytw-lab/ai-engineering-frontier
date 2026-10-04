# Knowledge files

`inbox/` 是待處理區，`inbox/processed/` 保存已成功轉換的原檔，`raw/` 保存固定格式的 Markdown。Day 8 的 [`convert.py`](convert.py) 由使用者在終端機執行；它使用 [`source-to-raw-md`](../skills/source-to-raw-md/SKILL.md) 的轉換與驗證程式，不需要 Qwen 呼叫 skill。

目前有五份自行撰寫的虛構 `harbor-api` 文件，用於後續檢索實驗：

```text
knowledge/inbox/processed/api-spec.md    已處理原檔
knowledge/raw/doc-fe96deca8c6c492f.md   轉換結果
```

把 `.txt`、`.md`、`.markdown`、有文字層的 `.pdf`、`.html` 或 `.htm` 放入 `knowledge/inbox/`，在專案根目錄執行：

```bash
uv run --with pypdf --with fonttools python knowledge/convert.py
```

程式會處理待處理區中所有支援的檔案，逐份核對 raw 與原件，成功後才把原檔移入 `processed/`。下次執行會略過 `processed/`。失敗或格式不支援的檔案留在待處理區，並在終端機顯示原因。也可以單獨重查整個 `raw/`：

```bash
uv run --with pypdf --with fonttools python skills/source-to-raw-md/scripts/validate.py knowledge/raw
```

PDF 每頁都有標記，但圖表、公式、表格與雙欄順序要對照原檔；掃描 PDF 需要先做 OCR。只靠 JavaScript 顯示正文的網頁也不在目前範圍。Day 11 的 [`wiki.py`](wiki.py) 會從 `raw/` 自動建立 `wiki/index.md` 與 `wiki/sources/`，使用者不需要手動替來源文件分類。Day 10 的 [`retrieve.py`](retrieve.py) 會從 Day 9 的 chunk manifest 建立 SQLite FTS5 索引，回傳帶來源位置的候選 chunks；Day 14 的 [`rag.py`](rag.py) 將這些候選經 context builder 篩選後交給本地 Qwen。

重建 source catalog：

```bash
uv run python knowledge/wiki.py
```

source pages 只提供來源導覽與 provenance，完整正文仍以 `raw/` 為準。

Day 13 的 [`context.py`](context.py) 會接收 `retrieval.sqlite` 的候選 chunks，先扣除 system prompt、history、tool schema 和 output reserve，再依來源位置與 token budget 組出 bounded context。它只組裝 messages，不會啟動模型；被淘汰的 chunks 和原因也會保留下來供診斷。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/context.py \
  --query 'production release' \
  --context-window 1024 \
  --output-reserve 128
```

Day 14 問答入口會先重建 FTS5 索引，再取得附來源的回答或明確拒答。沒有選入證據時不呼叫模型；每次執行將問題、完整 context、模型回應與耗時附加到 `runs/day14-rag.jsonl`。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/rag.py \
  --query production \
  --question 'production 的 HARBOR_WORKER_COUNT 是多少？' \
  --model mlx-community/Qwen3.8-27B-4bit
```

加上 `--dry-run` 可先檢查選入證據與 tokens，省略時需要已啟動本地 runtime。用 `--checkpoint` 可跑三個固定案例；命令與實測見 [Day 14 驗證紀錄](../docs/day14-verification.md)。

這五份示範文件不含真實公司資料、秘密或個人資料。`incident-runbook.md` 裡的英文指令句是刻意加入的測試資料，不是系統指令。

## Day 15：唯讀工具呼叫

Day 15 的 `list_sources` 只讀 `index/manifest.json`，回傳來源檔名和 document ID；當時不讀正文、不接受路徑參數，也不寫入檔案。Python 會檢查工具名稱與參數，並限制每回合最多執行一個工具。

啟動本地 runtime 後，可執行兩個模型選擇案例：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
```

一題要求篩選 `deployment` 來源，另一題是簡單算術，檢查模型是否會在不需要工具時直接回答。程式限制的單元測試與實測紀錄見 [Day 15 驗證紀錄](../docs/day15-verification.md)。

## Day 16：依文件 ID 讀取片段

`tools.py` 新增 `get_document_chunks`，從 `index/manifest.json` 依完全相符的 document ID 取回內容。每次最多提供 3 個 chunks，每個 chunk 保留 ID、raw 行號、token 數和文字；回應也會標示實際回傳數量與是否截斷。工具只讀 manifest，不接受路徑或檔案名稱參數，也不會修改檔案。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
uv run python -m unittest tests.test_day16_tools -v
```

單回合最多執行一個工具，因此目前要先知道 document ID；`list_sources` 列出 ID 後，需另開一回合讀取片段。`get_document_chunks` 會把文件內容當待分析資料，提示模型不要遵循內容中的操作要求；這段 prompt 提示本身不構成安全保證。驗證紀錄見 [Day 16 驗證紀錄](../docs/day16-verification.md)。

## Day 17：搜尋並匯入使用者選定的網頁來源

`tools.py` 新增 `web_search` 與 `import_web_source`。前者回傳最多 5 筆搜尋候選，並把候選 ID 暫存在被 Git 忽略的 `runs/day17-web-search.json`。它不下載頁面、不寫入知識庫。下一輪只有在使用者明確選定候選（例如「我選第 2 筆，請匯入」）時，模型才能用 `import_web_source` 指定 `web-2`。

匯入工具只會讀取最近一次搜尋產生的 ID，不接受任意 URL 或檔案路徑。程式以 HTTP/HTTPS 擷取所選頁面，拒絕本機／內部 IP、超過 20 MiB 的來源和不支援的內容格式；原始快照與網址、標題、中繼資料存入 `inbox/`，再交給 `source-to-raw-md` 的既有 batch converter，完成後原件會移到 `inbox/processed/`，標準化 Markdown 寫入 `raw/`。接著重建 manifest 和 SQLite FTS5 索引，讓新來源可以被本地檢索使用。

目前預設搜尋端點是 DuckDuckGo Lite。若服務要求人工驗證或解析不到結果，工具會回報失敗，不會自動匯入搜尋摘要。只支援靜態 HTML、文字和 PDF；JavaScript-only 網頁或沒有可抽取文字的 PDF 會留在待處理區。

啟動本地 runtime 後，`--checkpoint` 會驗證模型是否選對工具、Python 是否回傳檢查結果：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
uv run python -m unittest tests.test_day17_tools -v
```

搜尋結果與使用者選取必須分成不同回合；每回合仍最多執行一個工具。文章見 [Day 17](../articles/day17.md)，實測細節見 [Day 17 驗證紀錄](../docs/day17-verification.md)。
