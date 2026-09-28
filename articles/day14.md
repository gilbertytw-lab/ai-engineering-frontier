# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 14：將知識庫與模型結合，做出有來源的 RAG

Day 13 完成了 `knowledge/context.py`，能排除重複的文件片段，再挑出放得進 token 預算的證據。今天把這些證據交給本地 Qwen，讓模型回答問題，並標出回答用了哪些片段。

這次新增 `knowledge/rag.py`，把搜尋、挑選證據、呼叫模型和檢查引用串起來。接上自己的文件後，就能照著範例提問，並查看回答的來源；文件缺少答案時，模型會被要求明確回答不知道。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天的整段流程

檢索增強生成（Retrieval-Augmented Generation，RAG）結合外部資料檢索與模型生成。這篇的做法，是先從文件找出短證據，再讓模型根據證據回答。研究出處可看 [Lewis 等人的 RAG 論文](https://arxiv.org/abs/2005.11401)。

沿用前幾天建立的資料層，現在整段流程是：

```text
raw 文件 → chunk manifest → FTS5 搜尋
    → context.py 去重與預算檢查
    → 本地 Qwen 回答 → rag.py 檢查引用
```

搜尋先找出相關片段，`context.py` 再排除重複內容、檢查預算，把選好的證據放進模型輸入（prompt）。Qwen 根據這些內容回答，程式則查回引用片段的來源檔名與行號，供讀者核對。

今天主要操作的程式是 `knowledge/rag.py`。它每次啟動都會從文件與片段清單（manifest）重建 FTS5 搜尋索引；新增或修改 raw 文件後，要先重建 manifest，搜尋才會用到更新後的內容。

## 先準備資料，再啟動模型

以下命令都在專案根目錄執行，沿用前幾天的環境。本次使用 macOS Apple Silicon、Python 3.13.15、`mlx-lm 0.31.3`，模型是 `mlx-community/Qwen3.8-27B-4bit`。

如果 raw 有變更，先重建 manifest：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24
```

`HF_HUB_OFFLINE=1` 會讓程式只讀取本機快取。執行前，必須先下載本篇使用的 Qwen 模型與 tokenizer；環境準備方式沿用 Day 2 的步驟。

接著在終端機一啟動本地 runtime：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

保持這個終端機開著，在終端機二執行問答：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/rag.py \
  --query production \
  --question 'production 的 HARBOR_WORKER_COUNT 是多少？production 錯誤率持續多久、高於多少時要停止放量並回滾？請分別引用設定文件與部署文件。' \
  --model mlx-community/Qwen3.8-27B-4bit
```

`--query` 是搜尋關鍵字，`--question` 是要問模型的完整問題。目前多個關鍵字採 AND 比對，片段必須同時包含這些詞才會命中。因此我用文件裡確實出現的 `production` 搜尋，再用中文描述問題。換成自己的文件時，可以先用服務名稱或設定鍵查找。

想先查看模型會拿到哪些證據，可以在上面的問答命令加上 `--dry-run`。程式會組裝輸入並保存紀錄，不呼叫模型。每次執行都會在 `runs/day14-rag.jsonl` 追加一筆資料，選入的文字與來源放在該筆紀錄的 `context.selected_chunks`。

## 回答要附來源，引用也要經過檢查

Day 5 已經練習過 JSON 回答。今天採用三個欄位：

```json
{
  "answer": "production 的 HARBOR_WORKER_COUNT 預設值為 8。",
  "citations": ["doc-3317e1a5be5eb33f-chunk-0002"],
  "no_answer": false
}
```

這是格式示例。`answer` 放回答，`citations` 放用到的完整 chunk ID，`no_answer` 表示資料是否不足。

有答案時，至少要引用一個 chunk，而且引用必須來自本次實際送入 prompt 的證據。被 context builder 排除的 chunk，即使仍存在資料庫裡，也不能被引用。

模型產生回答，並列出用到的 chunk ID。來源檔名、raw 路徑和行號都由程式依 ID 查回，避免模型自行填寫位置。

這次跨文件問題的實際回答是：

> production 的 HARBOR_WORKER_COUNT 預設值為 8。當 production 錯誤率連續 5 分鐘高於 2% 時，需停止放量並回滾到上一個 stable release。

程式查回兩個來源：`service-config.md` 的 raw 第 23–34 行，以及 `deployment-guide.md` 的 raw 第 25–33 行。我回看文件，worker 的 `8` 與回滾門檻都有對上。

這題只問觸發門檻；部署文件還有資料庫 migration 的處理條件，實際回滾時仍要閱讀完整流程。

## 找到文件，也可能沒有答案

我另外用 `log retention` 搜尋，問 `harbor-api` 的 log retention 是幾天。搜尋有命中，但文件明確寫著沒有定義這項政策。模型回答：

> 不知道，提供的證據明確指出 release-policy.md 沒有定義 log retention，且未提供 harbor-api 相關的其他文件資訊。

這時 `no_answer=true`，`citations` 是空陣列；模型看過的證據仍保存在執行紀錄中，可以回查拒答原因。

搜尋完全沒有命中時，程式直接回覆不知道，省下這次模型呼叫。如果模型已經拿到證據，卻找不到問題所需的資訊，就由模型判斷是否拒答；這個判斷仍可能出錯。

## 有來源，還是要核對答案

今天把模型輸入與輸出預留的合計上限設為 2,048 tokens，其中保留 512 給 JSON 回答。計算輸入長度和發送請求時，都使用 `enable_thinking=false`，讓兩邊採用相同的對話模板（chat template）設定。這是本次測試的預算，換模型或問題時仍要重新量測。

程式也會檢查模型是否正常結束。若 `finish_reason=length`，代表碰到輸出上限，這份回覆會記錄為失敗。

這些檢查能確認格式、引用與來源位置，還無法保證每句回答都被證據支持。例如模型寫成「worker 數量為 80」，卻引用正確的設定 chunk，引用存在性檢查仍會放行。

第二週走到這裡，讀者已經能把文件轉成 raw、建立索引、挑出預算內的證據，再取得附來源的本地回答。本次驗證的三個固定案例都通過：跨文件回答、文件沒有定義答案，以及搜尋零命中；既有紀錄也顯示全專案 49 個測試通過。

先拿一個自己知道答案的問題試跑。回答出現後，打開它引用的 raw 行號，確認數字和條件真的在那裡。

## 參考資料

- 系列前篇：Day 13〈Context 預算控管〉
- [RAG 原始論文](https://arxiv.org/abs/2005.11401)
- [MLX-LM server 官方文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
