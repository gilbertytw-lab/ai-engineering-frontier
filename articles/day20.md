# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 20：MCP 解決了什麼問題？

Day 19 把模型回傳的參數（`arguments`）交給 Python 再檢查一次：欄位、型別和長度都通過後，才呼叫對應的處理函式（handler）。目前四個工具的工具結構描述（schema）、參數驗證和執行都由 `knowledge/tools.py` 負責。

改用模型上下文協定（Model Context Protocol，MCP）後，工具的探索與執行會經過 MCP 用戶端（client）和伺服器（server）。目前專案儲存庫（repository）還沒有 MCP client 或 server；以下依現有程式碼和 MCP 官方文件比較架構，沒有實作轉接器（adapter）。

## 先分清兩段流程

本專案目前的流程是：

```text
TOOL_SCHEMAS 交給 Qwen
    ↓
Qwen 回傳 `tool_calls`（工具呼叫資料）
    ↓
Python 分派器（dispatcher）檢查名稱與 arguments
    ↓
呼叫本機 Python handler
    ↓
工具結果交回 Qwen
```

`TOOL_SCHEMAS` 列出 Qwen 可用的工具與參數。分派器（dispatcher）檢查模型回傳的工具名稱和 `arguments`，再交給 `knowledge/tools.py` 中對應的函式：`list_sources`、`get_document_chunks`、`web_search` 或 `import_web_source`。

MCP 定義 AI 應用程式主機（host）和外部工具 server 之間的溝通方式。host 負責管理應用程式體驗，也可以連接多個 server；每個 server 都有自己的 client。client 透過 `tools/list` 探索 server 提供的工具，再用 `tools/call` 請 server 執行指定工具。MCP server 也能提供資源（resources）和提示範本（prompts）。

```text
AI 應用程式（MCP host）
    ├─ MCP client A ⇄ MCP server A
    └─ MCP client B ⇄ MCP server B
```

## 直接工具和 MCP 的差別

| | 直接提供工具函式 | 透過 MCP 整合 |
|---|---|---|
| 工具描述從哪裡來 | 應用程式自己的 `TOOL_SCHEMAS` | MCP client 向 server 用 `tools/list` 取得 |
| 怎麼執行 | dispatcher 呼叫本機 Python handler | client 用 `tools/call` 請 MCP server 執行 |
| 適合的情況 | 單一應用程式、少量自有工具 | 多個支援 MCP 的應用程式要重用同一個 server，或需要接既有 MCP server |
| 多出的工作 | 維護工具 schema、dispatcher 與 handler | 維護 MCP client/server、連線設定與兩側的錯誤處理 |

如果不同 AI host 都要重用同一組工具，MCP 的好處就很明確：每個 host 都能用同一協定探索並呼叫同一個 server。server 也可以在這個介面提供 resources 和 prompts。

MCP 不會替模型選工具，也不會自動把應用程式現有的 Python 函式變成可用服務。host 仍要把工具資訊提供給模型；模型回傳選擇後，MCP client 才會透過 `tools/call` 請 server 執行。

## 這個專案現在需要 MCP 嗎？

目前 repository 只有一個本地 AI 助理和四個工具。直接呼叫少了 MCP client/server 與連線管理，沿著 `knowledge/tools.py` 就能追到執行流程。

如果之後要讓另一個 AI 應用程式重用知識工具，或連接現成的 MCP server，再評估加入 MCP 轉接器。即使改走 MCP，Python 端的允許清單（allowlist）、`arguments` 驗證和使用者選取檢查仍要保留。協定提供工具探索與呼叫方式；工具實際能做什麼，仍由 server 和應用程式規則限制。

這次沒有實測 MCP 的延遲、整合工時或跨 host 相容性。能確認的是兩者位於不同層：Qwen 回傳的 `tool_calls` 是模型提出操作的資料，MCP 則是 host 和外部工具 server 溝通的協定。這個專案目前沒有跨 host 重用需求，直接呼叫工具函式就足夠。

## 參考資料

- [MCP 官方：What is MCP?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)
- [MCP 官方：Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [MCP 官方：Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts)
- [AI Engineering 研究前線專案程式碼](https://github.com/gilbertytw-lab/ai-engineering-frontier)
