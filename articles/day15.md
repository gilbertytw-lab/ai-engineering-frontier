# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 15：告訴模型能用哪些工具，程式再決定怎麼執行

Day 14 我完成了有來源的 RAG：Python 搜尋文件、挑出證據，再由本地 Qwen 根據證據回答。Day 15 要讓 Qwen 遇到需要查目錄的問題時提出工具呼叫，再由程式驗證並執行。

模型只提出工具名稱與參數；Python 驗證請求後才執行對應功能。Qwen 無法跳過程式直接讀取檔案。

今天新增一支 Python 程式，定義唯讀工具 `list_sources`。程式會把工具清單送給 MLX-LM，驗證模型回傳的呼叫，再把查詢結果交回模型組成回答。

[專案程式碼](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 從回答問題到請程式做事

Day 14 的流程由 Python 先跑完搜尋和 context 組裝，Qwen 只收到證據與問題：

```text
問題 → Python 搜尋與挑選證據 → Qwen 根據證據回答
```

加入工具後，模型可以在回答之前提出一個工具呼叫：

```text
問題 → Qwen 選擇工具與參數 → Python 驗證並執行
     → 工具結果回到 Qwen → Qwen 整理回答
```

工具呼叫是模型提出的請求，工具清單和執行權仍由應用程式掌握。OpenAI 的 function calling 文件也採用相同的往返概念：提供工具、接收模型提出的呼叫、由應用程式執行，再把結果交回模型。[官方流程說明](https://developers.openai.com/api/docs/guides/function-calling)

## 先把工具契約寫清楚

今天只提供一個工具：`list_sources`。它能列出知識庫的來源文件，也能依檔名片段篩選。送給 MLX-LM 的結構描述（JSON Schema）如下：

```json
{
  "type": "function",
  "function": {
    "name": "list_sources",
    "description": "列出知識庫來源文件，可依檔名片段篩選；不讀取文件內容。",
    "parameters": {
      "type": "object",
      "properties": {
        "name_contains": {
          "type": "string",
          "description": "檔名片段；空字串代表列出全部來源。"
        }
      },
      "required": ["name_contains"],
      "additionalProperties": false
    }
  }
}
```

`name` 是程式實際註冊的函式名稱；`description` 幫助模型判斷什麼情況該用它；`parameters` 描述呼叫時接受的輸入。這裡只有一個字串參數，沒有檔案路徑欄位。

可以把 schema 想成菜單：它列出能點什麼、點餐要附哪些資料；真正準備結果的還是程式。

單有 schema 還不夠。模型輸出仍要經過程式檢查，因為格式符合不代表操作就安全。

## 程式把工具範圍鎖小

`list_sources` 只讀固定的來源清單檔 `knowledge/index/manifest.json`，回傳來源檔名和 document ID。模型不能指定路徑，也拿不到文件正文。程式接著會檢查：

- 函式名稱必須在 `list_sources` 允許清單內。
- arguments 必須是合法 JSON object，且只能有 `name_contains`。
- 篩選值必須是字串，最多 80 個字元；重複欄位也會被拒絕。
- 單一回合最多執行一個工具，最多呼叫模型兩次：一次決定與呼叫工具，一次整理工具結果。

即使模型回傳 `delete_source`，或在參數中加入 `path: "/etc/passwd"`，工具分派器（dispatcher）也不會把請求交給任何函式。這個工具沒有刪除或寫入檔案的程式碼。

## 讓 Qwen 實際選一次

先啟動本機 server：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

另開一個終端機，以 `--checkpoint` 執行兩個測試案例：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
```

第一題要求列出檔名包含 `deployment` 的來源。Qwen 呼叫 `list_sources`，傳入 `{"name_contains":"deployment"}`。程式從來源清單讀出 `deployment-guide.md` 和對應的 document ID，再把結果交回模型；第二次請求最後回答 `deployment-guide.md`。

第二題問「2 加 2 等於多少」，並同樣提供工具清單。Qwen 直接回答「2 加 2 等於 4」，`tool_call_count=0`。

這兩個案例展示工具呼叫的往返流程，Qwen 依結構描述提出工具名稱與參數，Python 透過 allowlist、參數檢查和固定來源清單決定是否執行。每回合最多執行一個工具，而 `list_sources` 只回傳來源名稱和 ID。新增工具時，輸入範圍與執行限制也要寫進程式。

Day 16 會新增第一個內容工具：讓程式依文件 ID 查詢受限的文件片段，再把唯讀證據交給模型。

## 參考資料

- 系列前篇：Day 14：將知識庫與模型結合，做出有來源的 RAG
- [OpenAI function calling 官方文件](https://developers.openai.com/api/docs/guides/function-calling)