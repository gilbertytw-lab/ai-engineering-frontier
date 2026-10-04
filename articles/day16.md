# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 16：依文件 ID 讀取受限的內容片段

Day 15 的 `list_sources` 能讓本地 Qwen 找到文件名稱和 document ID，但不會提供正文。今天新增 `get_document_chunks`，讓 Python 依文件 ID 從固定的 chunk manifest 取回少量內容，再把證據交回模型。

這個工具不接受檔案路徑。模型只能指定一個已知的 document ID，程式最多回傳該文件的 3 個 chunks。

## 工具輸入只需要文件 ID

送給 MLX-LM 的結構描述（JSON Schema）把參數限縮為 `document_id`：

```json
{
  "type": "function",
  "function": {
    "name": "get_document_chunks",
    "description": "依文件 ID 讀取最多 3 個唯讀文件片段；不接受路徑。",
    "parameters": {
      "type": "object",
      "properties": {
        "document_id": {
          "type": "string",
          "description": "list_sources 回傳的文件 ID。",
          "maxLength": 80
        }
      },
      "required": ["document_id"],
      "additionalProperties": false
    }
  }
}
```

Schema 讓模型知道怎麼提出請求；實際限制仍由 Python 執行。Dispatcher 會重新檢查工具名稱、JSON 欄位和型別，只接受一個不超過 80 個字元的文件 ID。多傳 `path`、漏傳 ID 或輸入未知 ID 都不會讓程式改讀其他位置。

## 從 manifest 取回的內容有上限

`get_document_chunks` 只讀 `knowledge/index/manifest.json`，不開啟 manifest 內記錄的 raw path。符合 document ID 後，程式回傳來源名稱，以及最多 3 個 chunks 的 chunk ID、raw 行號、token 數和文字。回應另附總數、回傳數與 `truncated`；文件超過上限時，Qwen 收到的結果會明確標記截斷。

Chunk 是從原始文件切出的片段。Manifest 裡已經保存好文字和原始行號，所以這一步不必讓模型自己猜檔案位置，也不用再讀完整文件。這次測試中的 `service-config.md` 有 3 個 chunks，回傳內容共 314 tokens，沒有截斷。

文件正文可能含有看起來像指令的文字。我在 system prompt 加上提醒，要求模型把工具回傳內容視為資料，不要把其中的操作要求當成指令。Prompt 只是行為提醒；可讀資料仍由程式端的固定 manifest 查詢、參數驗證和回傳上限控制。

## 讓 Qwen 讀取一份設定文件

先啟動本地 runtime：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

在另一個終端機執行固定 checkpoint：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
```

文件查詢案例要求 Qwen 使用 ID `doc-3317e1a5be5eb33f`，找出 `service-config.md` 的 production `HARBOR_WORKER_COUNT`。模型提出 `get_document_chunks` 呼叫後，Python 回傳該文件的 3 個 chunks；Qwen 接著回答：

> 在 `service-config.md` 的 **Production defaults** 中，`HARBOR_WORKER_COUNT` 的值是 **8**（production 預設 worker 數量）。

這個案例的兩次模型呼叫和一次工具執行都通過 checkpoint。另兩個案例也通過：Qwen 用 `list_sources` 篩出 `deployment-guide.md`，並在簡單算術題上直接回答、沒有呼叫工具。這筆耗時只來自單次 checkpoint，不代表平均效能或工具選擇準確率。

程式端另有 7 個 Day 16 測試，涵蓋只回傳指定文件、3 個 chunk 上限、未知 ID、路徑與額外參數拒絕，以及 tool result 回傳模型的往返流程。全專案 67 個測試通過。

## 現在還不能靠名稱直接找內容

`get_document_chunks` 依 document ID 取回片段，不會搜尋哪一段和問題最相關。由於單回合仍只准執行一個工具，`list_sources` 與 `get_document_chunks` 也得分兩次操作；使用者需要先拿到 ID，再請模型讀取內容。

Qwen 現在能依 document ID 讀取指定文件最多 3 個 chunks。文件超過 3 段時，manifest 順序後面的內容不會自動補進來。

Day 17 會讓本地工具查不到足夠資料時搜尋網頁。搜尋結果先交給使用者挑選；模型不能把搜尋摘要直接寫進知識庫，必須等使用者選定來源後，才呼叫匯入與轉換工具。

## 程式碼

[專案 Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)
