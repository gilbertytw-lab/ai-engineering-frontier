# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 5：讓回答固定格式，先檢查模型交回來的 JSON

Day 4 已經把固定的 `system message` 放進每次請求，但 Runner 收到模型的 `message.content` 後就直接印出來。今天只改一件事：加上可選的 `--json-answer`，讓程式要求並檢查固定格式的回答。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## Day04 到 Day05 差在哪裡？

Day 04 的流程是：組出 `system` 和 `user` 兩則訊息，送到本地 runtime，再把文字回答印出來。

Day 05 在後面接了一層檢查：

```text
system + user
    ↓
本地模型回傳 message.content
    ↓
--json-answer：解析 JSON、檢查欄位與型別
    ↓
通過才輸出；失敗就回報錯誤
```

## 為什麼要要求 JSON？

Day 04 的文字回答適合直接給人看，卻不適合交給下一段程式處理。模型可能把結論、限制和補充說明混在同一段文字裡，程式很難穩定判斷哪一句該放進哪個欄位。

固定 JSON 格式等於替模型回答訂一個小型介面：`answer` 放主要回答，`limitations` 放限制。之後的程式可以直接讀欄位、判斷是否有缺資料、寫入紀錄，或把結果交給其他功能，不必靠關鍵字猜模型的句子。

這個改動改善的是資料交換，不是答案品質。模型仍可能在 `answer` 裡說錯話；JSON 通過，只代表資料形狀符合約定。

JSON 回答目前只有兩個欄位：

```json
{
  "answer": "主要回答",
  "limitations": ["回答的限制"]
}
```

`answer` 必須是非空白字串；`limitations` 必須是字串陣列，沒有要補充時使用 `[]`。省略 `--json-answer` 時，Day 04 的文字模式維持不變。

這個改動分成兩層。`JSON_ANSWER_PROMPT` 把格式要求放進 system prompt；`parse_answer()` 在模型回覆後檢查資料。提示詞只能要求格式，不能保證模型一定照做，所以程式仍要驗證。

## 如何驗證這次改動

先在專案根目錄跑自動測試：

```bash
uv run python -m unittest discover -s tests -v
```

這一步檢查 `parse_answer()`、請求 payload、文字模式、錯誤處理與互動模式。測試使用固定的 HTTP 回應，目的是確認程式邏輯，不是評估 Qwen 的回答品質。

接著啟動 Day 4 使用的本地模型：

```bash
uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

再用一個真正的 Day 05 問題測試 JSON 路徑：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --temperature 0.2 \
  --max-tokens 1024 \
  --json-answer \
  '請用 JSON 說明 system message 和 user message 的差別。answer 請用一句話，沒有限制時 limitations 使用空陣列。'
```

這個問題需要的資訊已經寫在 prompt 裡；模型不會自行讀取 Repository、測試檔或測試結果。若要讓模型檢查檔案，還要另外提供檔案內容或讀檔工具，這不是 Day 05 的範圍。

本次 Qwen 實際回傳：

```json
{
  "answer": "system message 用於設定模型的角色、行為與全局規則，而 user message 是用戶在對話中提出的具體問題或指令。",
  "limitations": []
}
```

命令結束碼是 `0`，代表這份回答通過 JSON 驗證。

驗證重點有兩個：命令結束碼是 `0`，而且 stdout 能被解析成包含 `answer` 和 `limitations` 的 JSON。這只證明本次請求走完「提示詞要求 → 模型回覆 → Python 驗證」；不代表模型每次都會回傳合法格式，也不代表答案內容已經查證。

## 今天留下什麼

Day 05 讓 Runner 多了一個可選的結構化輸出入口。程式現在知道回答長什麼樣子，還不知道回答是不是正確；後者要等之後加入資料與證據檢查才有辦法處理。

## 參考資料

- [Day 4：Prompt 到底改變了什麼？](day04.md)
- [Python 3.13：json.loads()](https://docs.python.org/3.13/library/json.html#json.loads)
- [MLX-LM server 官方文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
