# Day 15 驗證紀錄

查證日期：2026-09-29（Asia/Taipei）。記錄本機模型的工具呼叫、程式端限制與單元測試。

## 實作與環境

- Python 3.13.15、`mlx-lm 0.31.3`。
- 模型：`mlx-community/Qwen3.8-27B-4bit`，使用本機快取。
- endpoint：`http://127.0.0.1:8081/v1/chat/completions`。
- `knowledge/tools.py` 傳送標準 chat completion `tools` 欄位，使用 `temperature=0`、`enable_thinking=false`。
- 本機 `mlx_lm.server` 會讀取 `tools`；Qwen tokenizer 的 `has_tool_calling` 為 `True`。server 文件的 request fields 清單未提到 `tools`，因此另檢查安裝版本的 `server.py`／`tokenizer_utils.py`，再跑 live checkpoint。

唯一允許的工具是 `list_sources`。它讀取固定的 `knowledge/index/manifest.json`，只回傳 `source_name` 和 `document_id`；模型不能指定路徑，工具也不會讀取 raw 文件正文或修改檔案。

Dispatcher 重新檢查模型回應，不把 schema 當成安全邊界：工具名稱需在 allowlist、arguments 必須是 JSON object 且恰好包含 `name_contains`，其值必須是最多 80 字元的字串。重複 JSON 欄位、不支援的工具、額外參數、一次多個呼叫都會拒絕。工具執行後，第二次模型回應若又提出工具呼叫也會拒絕；程式上限是每回合最多一個工具呼叫、兩次模型請求。

## 真實 Qwen checkpoint

啟動 server：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

另一個終端機執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
```

實際輸出：

```text
Checkpoint tool_required：PASS
  model_calls=2，tool_call_count=1，elapsed_ms=5701.1
  tool=list_sources，arguments={'name_contains': 'deployment'}
  tool_result={"sources": [{"source_name": "deployment-guide.md", "document_id": "doc-891dc9cf617077c2"}]}
  answer=deployment-guide.md
Checkpoint tool_not_needed：PASS
  model_calls=1，tool_call_count=0，elapsed_ms=2116.5
  answer=2 加 2 等於 4。
Day 15 tool checkpoint：PASS
```

第一題要求列出檔名包含 `deployment` 的來源；Qwen 選擇 `list_sources` 並輸出符合參數，Python 執行後把工具結果交回模型，最後回答正確檔名。第二題是算術問題；工具清單仍有提供，Qwen 沒有呼叫工具並直接回答。

兩個案例各執行一次。延遲只記錄這次本機結果，不作平均效能或工具選擇準確率結論。

## 程式端限制測試

```bash
uv run python -m unittest tests.test_day15_tools -v
uv run python -m unittest discover -s tests -v
```

Day 15 的 11 個測試方法通過；全專案 60 個測試方法通過。新測試涵蓋：

- 唯讀清單只回傳來源名稱與 document ID。
- 不接受 allowlist 外的工具名稱。
- 不接受任意 `path` 或其他多餘參數。
- 拒絕重複 JSON 欄位、錯誤型別、超長篩選字串和非陣列 `tool_calls`。
- 多個工具呼叫會在執行前被擋下；工具結果回來後再次呼叫也會被擋下。
- 無工具需求時只呼叫模型一次；有工具需求時最多兩次，第二次會收到 tool result。

錯誤回應由測試直接交給 dispatcher，檢查程式不會呼叫 handler；它們驗證應用程式限制，不代表模型本身永遠不會產生錯誤請求。
