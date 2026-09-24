# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 9：將知識文件送入本地模型前要思考的事

Day 8 把五份 `harbor-api` 工程文件寫進 `knowledge/raw/`。雖然原始文件要完整留著，但每次問答不該把整個資料夾都送給模型。`raw` 負責回查，模型問答時只拿需要的知識片段。

如果每次 request 都把整個 `raw/` 資料夾送進模型，模型得處理大量用不到的內容；system prompt、問題、對話歷史、工具描述和輸出，也會一起佔用 context 預算。更麻煩的是，回答引用到一大份文件時，讀者很難知道真正使用的是哪一段。

所以要先把文件切成有位置標記的區塊（chunks）。每個 chunk 都能回到原始檔案的行號，也會記錄 token 數。後續搜尋只要挑出少量相關片段，問答程式就能在送出前算出證據包的大小。

「模型支援 32K context」只能告訴我們硬體條件導致的模型規格上限，不能直接當成 request 的可用空間。實際可用的空間還要扣掉 prompt、對話歷史、工具描述和輸出預留。同一個模型在不同電腦上，也可能因為記憶體和 runtime 設定不同而得到不同結果。

今天分兩步：先把 raw 文件切成可以回查原文位置的 chunks，再量測固定問題下不同長度 chunk 的 input tokens 和延遲。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天留下什麼

今天新增兩個入口：

- `knowledge/ingest.py`：讀取 `knowledge/raw/*.md`，產生 `knowledge/index/manifest.json`。
- `knowledge/measure.py`：用同一個 Qwen tokenizer 計算輸入長度，並選擇性呼叫本地 runtime 量測延遲。

資料流變成這樣：

```text
knowledge/raw/*.md
    ↓
Qwen tokenizer + 以換行作為邊界切分
    ↓
knowledge/index/manifest.json
    ↓
固定證據預算（evidence budget）組出 prompt
    ↓
本地 Qwen 問答與延遲量測
```

manifest 是可以刪掉重建的衍生檔，raw 才是原始文件。重新執行 ingest 就能產生同一份索引；如果手動改過 manifest，之後就很難確認回答引用的是哪一版文件。

## 先把文件切成可以回查來源的 chunks

我先選一個保守的測試設定：每個 chunk 最多 160 tokens，前一段最多重疊 24 tokens。這裡的 token 可以先理解成模型處理文字時使用的基本單位；它和字元數、中文字數都不是一比一。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24
```

這次的輸出是：

```text
建立 knowledge/index/manifest.json：5 份文件、11 個 chunks
```

每個 chunk 目前保存這些欄位：

```json
{
  "chunk_id": "doc-3a8e2b68f2b171e3-chunk-0001",
  "start_line": 12,
  "end_line": 29,
  "token_count": 138,
  "text_sha256": "...",
  "text": "..."
}
```

文件層還會保存 `document_id`、`source_name`、`source_snapshot`、raw 檔的 SHA-256 和原始來源的 SHA-256。回答拿到 chunk 之後，有兩條回查路徑。第一條是用 `chunk_id` 找 manifest，再用行號回到 raw；第二條是直接用 `text_sha256` 檢查這段文字是否被改過。

切分順序也刻意寫死了。程式先盡量在換行處收束，只有單行本身超過上限時才用 token slice 拆開。這比直接每 160 tokens 截一刀更適合 Markdown，標題、清單和段落比較不會被切成完全沒有上下文的碎片。

重跑同一個命令，manifest 的內容會完全相同。測試會比對整份 JSON，而不只比較 chunks 數量。文件內容改變時，raw hash 和 chunk hash 都會跟著變；文件沒變時，不會因為執行日期不同而產生新的版本。

## 先做 dry run，看看 prompt 實際有多長

今天先不做搜尋。為了量測輸入成本，`measure.py` 按照 manifest 順序拿 evidence，直到接近指定的 `evidence budget`。這裡的 evidence 是送進模型參考的來源 chunks；`evidence budget` 則是這些來源 chunks 可使用的 token 上限。這個選擇很刻意：今天先量「證據變多會發生什麼事」，Day 10 再處理「怎麼找到相關證據」。

不啟動模型也可以先看 tokenizer 計算的 input tokens：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/measure.py \
  --dry-run --evidence-tokens 160 320 640
```

本次 dry run 的結果如下。`requested budget` 是這次要求的 evidence token 上限；因為 chunk 必須完整放入，實際的 evidence tokens 可能低於這個數字。

| requested evidence | 實際 evidence tokens | Qwen input tokens |
|---:|---:|---:|
| 160 | 146 | 324 |
| 320 | 314 | 542 |
| 640 | 548 | 831 |

送進模型的 input tokens 不只來自文件內容，還包括 system prompt、問題、證據包裝文字，以及 Qwen chat template 加上的訊息標記。這就是為什麼第一組 evidence 只有 146 tokens，送進模型後仍然是 324 input tokens。

今天最有用的數字不是 160 或 640。是「我以為塞進 640，實際上 request 已經是 831」。context 預算如果只看 raw chunk 大小，通常會低估真正送出的 request。

## 三段輸入的實際結果

固定問題是：

> production release 前，最少要檢查哪些事項？如果資料不足，請明確說不知道。

這次量測把 `enable_thinking` 設為 `false`，因為要比較的是可交付回答的輸入與延遲；如果保留 thinking，回應可能只有 reasoning，沒有可讀的 `content`。量測使用本機快取的 `mlx-community/Qwen3.8-27B-4bit`，環境是 Python 3.13.15、`mlx-lm 0.31.3`，`max_tokens=128`。三次請求依序增加證據量：

```text
evidence=146 tokens，input=324 tokens，elapsed=23710.2 ms
evidence=314 tokens，input=542 tokens，elapsed=27303.4 ms
evidence=548 tokens，input=831 tokens，elapsed=29298.6 ms
```

整理成表格：

| 實際 evidence tokens | Qwen input tokens | 本次耗時 |
|---:|---:|---:|
| 146 | 324 | 23.7 秒 |
| 314 | 542 | 27.3 秒 |
| 548 | 831 | 29.3 秒 |

第一筆證據只有 `service-config.md` 的內容，模型回答不知道，這是合理結果：那份文件描述環境參數，沒有 release checklist 可供引用。第三筆證據增加 `release-policy.md` 後，模型才列出 CI、staging health check、canary 觀察與 rollback 目標等檢查事項。

這個結果不能拿來宣稱「每增加 500 tokens 就只多 5 秒」。我只跑了三次，而且都是同一台 Apple Silicon、同一個 server process、同一個固定問題。這三筆量測只支持兩個小結論：在這個環境裡，證據包變大時，request 延遲確實上升；證據不足時，模型有機會正確回答不知道。

## 27 項自動測試，外加三筆本機量測

除了實測，我也補了不需要啟動模型的測試：

- manifest 重建兩次後內容完全相同。
- chunk 不會超過設定的 token 上限。
- 每個 chunk 都保留文件行號和 hash。
- 超長單行會走 token slice，不會讓 chunk 無限長。
- evidence budget 會停止在不超過預算的完整 chunk。
- dry run 會計算 input tokens，但不呼叫 runtime。
- live measurement 會記錄耗時、回答 token 估計值與 thinking 設定。

完整回歸測試：

```bash
uv run python -m unittest discover -s tests -v
```

本次 27 項測試全數通過。測試驗證程式流程和資料契約；Qwen 的三筆數字則記錄這台機器上的實際 runtime。前者驗證流程，後者描述一次本機量測，兩者分開看。

## 今天的邊界

`manifest.json` 還不是檢索器（retriever）。它知道每段文字的位置和 token 數量，卻還不知道哪一段最適合回答使用者的問題。今天的量測範圍很小：一個固定問題、三個證據大小。它還稱不上完整的 benchmark suite，但已經足以支持一個工程決定：接下來不要把整個 raw 資料夾一次送進模型。

今天得到的順序很簡單：先固定來源版本，再建立可以回查的分段，最後才量測要放多少證據。少了前兩層，context budget 就沒有可靠的基準。

## 第一個可用的本機預算

今天留下兩個可以重跑的結果：一份可重建的 chunk manifest，以及一組本機 Qwen 的輸入／延遲量測。現在至少知道文件怎麼切，也知道送進模型後 request 會有多大。

目前還不能說這台機器穩定支援 8K、16K 或 32K 的有效問答 context。能確定的是，之後的預算計算必須包含 output reserve、system prompt 和對話歷史，而且已有一個可以重跑的量測入口。

Day 10 會在這份 manifest 上加入第一個真正的檢索路徑：先用關鍵字找候選 chunks，再比較「找到的證據」和「按照檔案順序塞進去」有什麼差別。

## 參考資料

- Day 8：為本地知識庫打地基
- [Qwen3.8-27B 模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [MLX-LM server 官方文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
