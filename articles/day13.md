# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 13：Context 預算控管

Day 12 比較了 raw、wiki 和 hierarchical 三條搜尋路徑。查詢 `production release` 時，FTS5 找到 5 個候選 chunks，其中兩個來自同一份 `release-policy.md`，而且行號重疊。

把這 5 個 chunks 全部送進模型，程式做得到；但每次 request 都還要支付 system prompt、問題、對話歷史、工具 schema 和輸出預留的 token 成本。證據能用的空間，只有扣完這些固定成本後剩下的部分。

所以今天新增 `knowledge/context.py`，在 evidence pack 送出前執行預算檢查、排序、去重，並留下每個候選被淘汰的原因。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天要完成的事情

今天新增一個 context builder。它接在 Day 10 的 SQLite FTS5 retriever 後面，今天先只組裝 messages，不啟動 Qwen：

- 先取得帶有 BM25 和來源位置的候選 chunks。
- 同一份文件的重疊行號只保留排名較前的 chunk。
- 把 system prompt、問題、history、tool schema 和 output reserve 算進 request 條件。
- 只有完整放入後仍不超過 context 預算的 chunks，才會進入最後的 messages。
- 保存選入和淘汰的候選，讓之後能追查「答案為什麼沒有看到某段資料」。

資料流現在變成：

```text
raw documents
    ↓
chunk manifest
    ↓
SQLite FTS5 candidates
    ↓
context.py：排序、重疊去重、budget check
    ↓
bounded messages
    ↓
下一篇才交給 Local LLM
```

這一日要固定下來的是 **bounded context**：一份有硬上限，而且每個候選都能回溯「為什麼被選入或淘汰」的模型輸入。

## 先算模型固定要吃掉多少

今天的預算公式很短：

```text
retrieval_budget =
  context_window
  - base_input_tokens
  - output_reserve
```

`base_input_tokens` 包括 system prompt、目前問題、既有 history、tool schema，以及 chat message 的包裝成本。`output_reserve` 是留給模型產生回答的額度；證據把輸入塞滿，模型可能還沒說完就撞到上限。

本次驗證把 `context_window` 設成 1,024、`output_reserve` 設成 128；這是沿用 Day 9 的測試設定，不是模型可用 context 的結論。

實際命令如下：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/context.py \
  --query 'production release' \
  --question 'production release 前，最少要檢查哪些事項？如果資料不足，請明確說不知道。' \
  --limit 5 \
  --context-window 1024 \
  --output-reserve 128
```

這次的 base input 是 124 tokens，因此留給 evidence 的 retrieval budget 是：

```text
1024 - 124 - 128 = 772 tokens
```

772 只是 raw evidence 的初步上限；最後仍要用同一個 Qwen tokenizer 重算完整 messages，因為 chat template、來源標頭和 evidence 包裝文字也會佔 token。

## 去重不是把排名後面的資料隨便砍掉

先看 FTS5 回傳的 5 個候選：

```text
1. release-policy.md（第 12–29 行，doc-3a8e2b68f2b171e3-chunk-0001）
2. deployment-guide.md（第 12–24 行，doc-891dc9cf617077c2-chunk-0001）
3. release-policy.md（第 26–34 行，doc-3a8e2b68f2b171e3-chunk-0002）
4. deployment-guide.md（第 25–33 行，doc-891dc9cf617077c2-chunk-0002）
5. service-config.md（第 32–35 行，doc-3317e1a5be5eb33f-chunk-0003）
```

`release-policy.md` 的兩個 chunks 重疊在第 26–29 行。Day 9 的 chunking 會保留 overlap，這對維持上下文有用；但如果兩段都原封不動送進模型，同一段文字就會算兩次。

`context.py` 先依 BM25 排序；同一份文件的行號重疊時，保留排名較前的候選，另一段標記成 `overlapping_lines_with`。真正相鄰、但沒有重疊的 chunks 不會被誤刪，所以 `deployment-guide.md` 的第 12–24 行和第 25–33 行都留下來。

這次去重後的結果：

```text
候選 5 個；去重後選入 4 個，淘汰 1 個
base input tokens=124，retrieval budget=772，final input tokens=723，output reserve=128
1. release-policy.md（第 12–29 行，doc-3a8e2b68f2b171e3-chunk-0001）
2. deployment-guide.md（第 12–24 行，doc-891dc9cf617077c2-chunk-0001）
3. deployment-guide.md（第 25–33 行，doc-891dc9cf617077c2-chunk-0002）
4. service-config.md（第 32–35 行，doc-3317e1a5be5eb33f-chunk-0003）
淘汰：doc-3a8e2b68f2b171e3-chunk-0002（overlapping_lines_with:doc-3a8e2b68f2b171e3-chunk-0001）
```

最後的 `input tokens` 是 723，加上預留的 128 後是 851，仍然低於 1,024。這裡沒有啟動 Qwen，因為今天要驗證的是「送出前如何挑資料」，還不是模型能不能回答正確。

## 被淘汰的證據也要留下紀錄

如果 context builder 只回傳選入的 chunks，之後遇到錯誤回答時，就無法分辨資料是沒被檢索到、因重疊被排除，還是因預算不足沒進 prompt。

所以 `ContextResult` 同時保存兩份清單：

```text
selected_chunks
rejected_chunks
```

目前的淘汰原因至少分成兩類：

- `overlapping_lines_with:<chunk_id>`：同一份文件的行號和較前候選重疊。
- `context_budget`：加入這段後，input 加上 output reserve 會超過上限。

這個分類還很小，卻比一句「模型可能漏看資料」有用得多。因為下一次可以直接問：是 retrieval 找錯，還是 budget 選擇太保守？

## history 和 tool schema 不能在公式裡消失

今天的 CLI 範例沒有傳入對話歷史或工具 schema，但 `build_context()` 已經把兩者當成正式參數。測試用一個前一輪 user message 和一個 `list_sources` 的唯讀工具 schema，確認它們會一起進入 system／history 的 token 計算。

即使目前沒有 tool calling，也不能把 tool schema 從公式拿掉；同樣地，現在只有一輪問題，也不代表之後不會帶入 history。若 budget 公式先把它們省略，功能一加進來，證據上限就會靜默膨脹。

這次沒有選擇把 context window 變大來掩蓋問題。先把每個固定成本算進去，之後不管加入工具還是保留幾輪對話，都能看到證據空間被吃掉多少。

## 3 個 Day 13 測試方法，38 個全專案測試

Day 13 新增 [`knowledge/context.py`](../knowledge/context.py) 和 [`tests/test_day13_context.py`](../tests/test_day13_context.py)。測試先不碰本機模型，只檢查 context 組裝的資料契約：

- 重疊 chunks 保留較高排名者；相鄰 chunks 維持可選。
- history 和 tool schema 確實算入 base input tokens。
- 超過預算的候選會被拒絕，並保存原因。
- 反轉候選輸入順序後，排序和選入結果不變。

執行：

```bash
uv run python -m unittest tests.test_day13_context -v
uv run python -m unittest discover -s tests -v
```

結果是 Day 13 的 3 個測試方法通過，全專案 38 個測試通過。這一日沒有新增 Qwen latency 數字；context 組裝和模型回答分開驗證。

## 今天留下的邊界

`context.py` 解決的是「哪些證據可以進 prompt」，還沒有解決「回答怎麼引用它們」。目前的檢索仍然是 FTS5 的 lexical retrieval；去重會檢查 chunk ID、文字雜湊，以及同一份文件的行號重疊，但還沒有做語意相似度判斷。

1,024 和 128 是今天的測試設定，不是硬體能力的結論。真正部署時，仍然要用固定題目集觀察回答長度、延遲、引用正確性（citation correctness），以及資料不足時的拒答（no-answer）行為。

今天比較像替 RAG 裝上一個限流閥：水管裡有哪些水，交給 retriever；一次讓多少水流進模型，交給 context builder。限流閥不會讓水變乾淨，但至少知道哪一滴水被擋在外面。

## 一個可以被重跑的 evidence pack

到今天，從查詢到模型輸入之前，已經有一段可以單獨驗證的路徑：

```text
問題
  → FTS5 候選
  → BM25 排序
  → 重疊去重
  → base input 與 output reserve
  → bounded messages
```

這一步讓「context 不夠」從模型的神祕失誤，變成一個可以查數字、查 chunk、查淘汰原因的工程問題。

下一篇會把這份 bounded context 交給本地 Qwen，補上來源引用、資料不足時的 no-answer，以及一個可以重建和量測的 RAG checkpoint。

## 參考資料

- [Day 9：將知識文件送入本地模型前要思考的事](day09.md)
- [Day 10：資料分段後的查詢手法](day10.md)
- [Day 11：知識庫不能只是關鍵字搜尋](day11.md)
- [Day 12：同一個問題，三種資料搜尋路徑的差異在哪裡？](day12.md)
- [Knowledge files](../knowledge/README.md)
- [設計決策紀錄](../docs/design-decisions.md)
