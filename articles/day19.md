# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 19：調用工具有固定格式，如果參數錯誤怎麼辦？

Day 18 用 10 題檢查 Qwen 會不會選對工具，這 10 題都命中。不過，那次評估只比對工具名稱；模型帶來的參數（arguments）有記錄，沒有評分。

工具選對了，參數還是可能填錯。像 `list_sources` 只接受 `name_contains`，如果模型多塞一個 `path`，程式就不能把整包資料直接交給工具函式。

## Schema 告訴模型怎麼呼叫，Python 再檢查一次

工具的 JSON Schema 會隨請求送給模型，列出工具名稱、可用欄位、型別，以及能否帶入額外欄位。以 `list_sources` 為例，它只接受一個字串欄位 `name_contains`，而且 `additionalProperties` 設為 `false`。

但模型回傳的工具呼叫仍是外部輸入。`knowledge/tools.py` 收到回應後，會先檢查呼叫格式與工具名稱，再解析 arguments、驗證欄位和內容，最後才執行對應的 Python 函式。Schema 幫模型理解介面；dispatcher 的檢查決定程式是否接受這次請求。

例如這個參數多帶了 `path`：

```json
{
  "name_contains": "deploy",
  "path": "/tmp/secret"
}
```

`list_sources` 只接受 `name_contains`，所以 dispatcher 會回報「`list_sources` 只接受 name_contains 參數」，不會呼叫 `list_sources()`。

## 驗證的不只是欄位名稱

`parse_tool_arguments()` 先要求 arguments 是 JSON 字串，解析後必須是 object；同一個 JSON object 若重複出現欄位名稱，也會拒絕。接著才依工具逐項檢查：

- `list_sources` 只接受 `name_contains`，值必須是字串，最多 80 個字元。
- `get_document_chunks` 只接受非空的 `document_id`，最多 80 個字元。
- `web_search` 只接受非空的 `query`，最多 300 個字元。
- `import_web_source` 只接受 `web-1` 到 `web-5` 這種 `source_id`。

欄位檢查通過後，`import_web_source` 還會確認目前這一輪的使用者訊息有明確選定該來源，才呼叫匯入函式。參數格式正確，並不等於這個操作已獲得使用者同意。

## 用測試確認錯誤請求不會執行

測試會把 `list_sources()` 換成一個只要被呼叫就立刻失敗的替身，再讓模擬模型回傳包含 `path` 的參數。預期結果是收到 `ToolCallError`；如果程式真的呼叫了工具函式，測試會直接失敗。其他測試也涵蓋重複欄位、錯誤型別、超過長度上限、未知工具和一次提出多個工具呼叫。

這些案例透過模擬 completion 將資料交給 dispatcher，檢查應用程式如何拒絕輸入；它們沒有證明 Qwen 永遠不會產生錯誤參數。若要在專案中重跑相關測試：

```bash
uv run python -m unittest tests.test_day15_tools tests.test_day16_tools tests.test_day17_tools -v
```

Day 18 檢查 Qwen 選了哪個工具；Day 19 檢查 Python 收到請求後，會不會在執行前拒絕不合規的參數。工具呼叫的選擇與執行，各有一道不同的檢查。

Day 20 會比較直接提供工具函式與 MCP（Model Context Protocol）的差別。

## 程式碼

[專案 Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)
