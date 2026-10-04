# Day 16 驗證紀錄

驗證日期：2026-09-30（Asia/Taipei）。記錄依 document ID 讀取唯讀文件片段、程式端輸入限制、真實 Qwen checkpoint 與單元測試。

## 實作與環境

- Python 3.13.15、`mlx-lm 0.31.3`。
- 模型：`mlx-community/Qwen3.8-27B-4bit`，使用本機快取。
- endpoint：`http://127.0.0.1:8081/v1/chat/completions`。
- 新增 `get_document_chunks` schema；參數只有 `document_id`，schema 和 dispatcher 都將長度限制為 80 個字元，額外欄位會被拒絕。
- dispatcher 會重新檢查工具 allowlist、JSON object、文件 ID 型別與長度。文件 ID 最多 80 個字元；不接受空字串、任意 `path` 或其他欄位。
- handler 只在固定 `knowledge/index/manifest.json` 中比對完全相符的 ID，不打開 raw path。每次最多回傳 3 個 chunks，保留來源名稱、chunk ID、raw 行號、token 數與文字；結果含總數、回傳數和 `truncated`。
- 未知 ID 回傳 `{"error":"找不到文件 ID"}`。超過 3 段時只回傳 manifest 順序最前面的 3 段。
- system prompt 提醒模型把文件內容視為待分析資料。這是模型行為提示，不是程式端安全限制。

## 真實 Qwen checkpoint

啟動本機 server：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

在另一個終端機執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
```

實際輸出摘要：

```text
Checkpoint tool_required：PASS
  model_calls=2，tool_call_count=1，elapsed_ms=10659.2
  tool=list_sources，arguments={'name_contains': 'deployment'}
  answer=deployment-guide.md
Checkpoint document_lookup：PASS
  model_calls=2，tool_call_count=1，elapsed_ms=18598.0
  tool=get_document_chunks，arguments={'document_id': 'doc-3317e1a5be5eb33f'}
  answer=在 `service-config.md` 的 **Production defaults** 中，`HARBOR_WORKER_COUNT` 的值是 **8**（production 預設 worker 數量）。
Checkpoint tool_not_needed：PASS
  model_calls=1，tool_call_count=0，elapsed_ms=2575.0
  answer=2 加 2 等於 4。
Day 16 tools checkpoint：PASS
```

文件查詢案例取得 `service-config.md` 的 3 個 chunks，總計 314 個 manifest tokens，`truncated=false`。工具結果包含 production 預設值 `HARBOR_WORKER_COUNT=8`，Qwen 回答的來源檔名和數值都符合測試條件。每個案例只執行一次；耗時是單次記錄，不作平均效能或工具選擇準確率結論。測試後已關閉本機 server。

## 程式端限制測試

```bash
uv run python -m unittest tests.test_day16_tools -v
uv run python -m unittest discover -s tests -v
git diff --check
```

Day 16 的 7 個測試方法通過；全專案 67 個測試方法通過。涵蓋範圍包括指定 ID 只會回傳該文件、最多回傳 3 個 chunks、截斷欄位、未知 ID、路徑與額外參數拒絕、空值／錯誤型別／超長 ID，以及 tool result 回到第二次模型呼叫。

## 驗收界線

- 這是依 document ID 的直接查詢，沒有根據問題搜尋或排序 chunks。
- 每次最多回傳 manifest 順序最前面的 3 個 chunks。較長文件的後續 chunks 不會自動補回；`truncated=true` 只指出資料不完整。
- 每回合仍限制一個工具呼叫，因此不能在同一回合先 `list_sources` 再 `get_document_chunks`。目前要先取得 ID，再另開一回合讀取。
- system prompt 的不可信內容提醒不能保證模型不會受文件文字影響；程式限制資料範圍，但沒有完成提示注入安全評測。
- 固定 checkpoint 只驗收三個例子，不能代表任務分布中的工具選擇能力。
