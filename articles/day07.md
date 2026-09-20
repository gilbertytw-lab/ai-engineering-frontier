# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 7：第一週交付前，先讓本地聊天程式跑完一次驗收

Day 06 讓互動模式真的帶上前一輪對話。到了第一週最後一天，我們做出的本地聊天程式（Chat Runner）已經可以單次呼叫、持續互動、加入 system message、驗證 JSON 回答，也能保留 Session history。

這五項能力各自有測試，還缺一個重要的確認：把它們串在同一條路徑上，會不會互相打架？

今天沒有加入新的 AI 概念。我把第一週收束成一個 `--checkpoint` 命令，讓它對真實的本地 Qwen3.8 連續發出兩個 request，同時驗收 JSON 格式與對話歷史。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天的驗收標準

這篇主文是 Level 1：啟動 runtime，再執行一條 checkpoint 命令。Level 2 可以替換 model 或 runtime URL；Level 3 則是修改驗收問題和判定條件。

Checkpoint 不是把 Day 02 到 Day 06 的命令再手動跑一遍。它固定了一組可機器判定的任務：

```text
第一輪：請記住代號「港口 17」，並以固定 JSON 回答「收到」
    ↓
把第一輪的 user / assistant message 放入 history
    ↓
第二輪：只問「上一題的代號是什麼？」
    ↓
回答必須是固定 JSON，answer 必須恰好等於「港口 17」
```

這條路徑同時用到四個已完成的零件：

- Day 04 的 system message。
- Day 05 的 JSON 格式要求與 `parse_answer()`。
- Day 06 的 Session history。
- Day 02 建立的本地 chat-completions HTTP 呼叫。

第二輪 prompt 裡沒有「港口 17」。如果程式沒有把第一輪送回模型，這個代號就沒有地方可以來。

## 為什麼不只看「能不能聊天」？

手動輸入幾句話，看到模型回答，只能證明畫面看起來可用。它沒有回答下列問題：

- 模型是否依照約定回傳 `answer` 與 `limitations`？
- JSON 通過時，內容是否也符合這次任務？
- 第二輪是否真的收到前一輪？
- 其中一步失敗時，命令是否用非零結束碼告訴 shell？

Checkpoint 把這些條件寫進 Python。回答只要少一個欄位、`limitations` 不是陣列、第一輪沒有回「收到」，或第二輪沒有回「港口 17」，這次驗收都會失敗。

格式正確不夠。這一天多加的，正是「答案有沒有做對這個小任務」的判定。

## `run_checkpoint()` 做了什麼

第一輪固定使用 `temperature=0` 和 `json_answer=True`：

```python
first_content = call_local_model(
    CHECKPOINT_FIRST_PROMPT,
    base_url=base_url,
    model=model,
    system_prompt=system_prompt,
    temperature=0,
    max_tokens=max_tokens,
    json_answer=True,
    history=history.copy(),
)
first_answer = parse_answer(first_content)
```

`call_local_model()` 已經會驗證模型回覆，回傳的是重新排版過的 JSON 字串。Checkpoint 再呼叫一次 `parse_answer()`，是因為接下來還要檢查 `answer` 和 `limitations` 的內容。

第一輪通過後，問題與完整的 JSON 回答才會加入 history：

```python
history.extend(
    [
        {"role": "user", "content": CHECKPOINT_FIRST_PROMPT},
        {"role": "assistant", "content": first_content},
    ]
)
```

第二輪沿用相同的 system message、JSON 規則與生成參數，只多了這份 history。最後會直接比對完整物件，不能只檢查回答裡有沒有代號：

```python
{"answer": "港口 17", "limitations": []}
```

這樣才能同時檢查欄位、型別與任務結果。

## 實際跑完第一週 checkpoint

先在終端機一啟動 MLX-LM server：

```bash
uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

等 server 開始監聽 `127.0.0.1:8081` 後，在終端機二執行：

```bash
uv run python frontier_knowledge.py \
  --checkpoint \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024
```

本次在 Python 3.13.15、mlx-lm 0.31.3 與 `mlx-community/Qwen3.8-27B-4bit` 的實際輸出是：

```text
Checkpoint 1/2：單次 JSON 回答通過（answer=收到）
Checkpoint 2/2：Session history 回答通過（answer=港口 17）
Day 7 checkpoint：PASS
```

命令結束碼是 `0`。Server log 也記錄了兩個 `POST /v1/chat/completions` 都回傳 HTTP 200。

如果 runtime 連不到、回傳非法 JSON，或第二輪答錯代號，程式會在 stderr 輸出 `Day 7 checkpoint：FAIL`，並以結束碼 `1` 離開。因此這條命令不只能給人看，shell 或後續的自動化流程也能判斷成功與失敗。

## 18 項自動測試守住哪些邊界

真實模型測試可以確認整條路徑跑得通，卻不適合當成每次都完全相同的回歸測試。模型輸出有它的不確定性，載入 27B 模型也會增加測試時間。

Day 07 因此另外加了 5 項不需要啟動 runtime 的測試：

- 第二輪呼叫會帶上第一輪的固定 JSON 回答。
- 第一輪沒有按約定回「收到」時驗收失敗。
- 第二輪沒有回正確代號時驗收失敗。
- HTTP 呼叫失敗時，checkpoint 回傳結束碼 `1`。
- `--checkpoint` 不接受單次 prompt、`--interactive`、`--no-history`、`--json-answer` 或 `--no-system-prompt` 這些衝突選項。

連同 Day 05 和 Day 06 的回歸測試，目前共 18 項：

```bash
uv run python -m unittest discover -s tests -v
```

本次結果為 18 項全數通過。

## 這個 checkpoint 還沒有證明什麼

`PASS` 的範圍很窄。它證明這支本地聊天程式在本次環境中能夠呼叫模型、驗證回答格式，並在第二輪找回前一輪的代號。

它還沒有檢查：

- 模型對真實工程問題的回答是否正確。
- 對話變長後，context 是否超出預算。
- 重開程式後，Session 能否恢復。
- 同時使用多個 runtime 或其他模型時，行為是否一致。
- 回答有沒有來自可查證的文件。

最後一點正好是第二週的主題。目前這支程式只會用模型已有的參數和當下 prompt 作答，還不會讀專案內的工程文件。

## 第一週留下什麼

今天增加的是一條可重複執行的本地聊天程式 checkpoint。它解決了「各功能分開看起來正常，合在一起卻沒有驗收」的缺口。

Day 08 會開始建立 `knowledge/raw` 與第一組工程文件。到那時，這支程式才有可以查找與引用的本地資料。

## 參考資料

- [Day 6：模型真的記得上一題嗎？](day06.md)
- [MLX-LM server 官方文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
