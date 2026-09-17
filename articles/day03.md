# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 3：讓模型可以連續處理多個問題

Day 2 的 `frontier_knowledge.py` 已經能把一個 prompt 送到 `mlx_lm.server`，讀回 JSON，再印出回答。問題也很明顯：每問一次，就得重新執行一次命令。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

今天把一次性呼叫改成互動式 Chat Runner。程式啟動後等待輸入，送出問題、顯示回答，再回到提示列。原本帶 prompt 的單次命令也保留。

## 今天要完成的目標

今天只處理命令列介面（CLI，Command-Line Interface）的使用流程：

- 省略 prompt 時進入互動模式。
- 每次輸入都送出一個獨立請求。
- 輸入 `exit`、`quit` 或 `:q` 時正常結束。
- 空白輸入不呼叫模型。
- 一次請求失敗時顯示錯誤，仍然可以繼續下一題。
- 保留 Day 2 的單次呼叫方式。

完成後，這個 CLI 可以反覆接受問題並回到輸入提示。每個問題仍然獨立處理，程式不會保存先前的問題與回答。

## 互動模式多了哪一步

Day 2 印出回答後就結束。Day 3 讓 CLI 回到輸入提示，等待下一個問題。

```text
啟動 frontier_knowledge.py
    ↓
等待使用者輸入
    ↓
空白？────是────→ 回到輸入提示
    │否
    ↓
退出命令？──是──→ 顯示結束訊息
    │否
    ↓
呼叫本地 runtime
    ↓
顯示回答或錯誤
    ↓
回到輸入提示
```

這個迴圈放在呼叫端，`mlx_lm.server` 不需要修改。server 每次只處理一個 HTTP 請求；等待下一題、判斷退出命令，都由 CLI 處理。

## 今天改了哪些檔案

今天改兩個檔案：

- `frontier_knowledge.py`：增加互動模式、退出命令與錯誤後繼續的流程。
- `README.md`：把專案目前進度更新到 Day 3，補上互動式執行命令。

這次沒有新增 Python 套件。單次模式和互動模式都呼叫既有的 `call_local_model()`，所以 HTTP 請求格式只維護一份。

另外，我在 `docs/design-decisions.md` 補上互動模式的責任邊界，在 `docs/originality-check.md` 登錄 Day 3 的檢查結果。這兩份文件是專案紀錄，不會影響讀者執行 CLI。

## 為什麼同時保留單次與互動模式

互動模式適合手動連續測試。單次模式則適合 shell script、重新產生固定輸出，或快速確認一個問題。兩種入口共用同一條 HTTP 呼叫路徑；之後修改 runtime 位址、模型名稱或產生參數時，只需要改一份請求格式。

單次模式仍然這樣執行：

```bash
uv run python frontier_knowledge.py \
  "請用一句話說明本地模型和網頁聊天 AI 的差別。"
```

省略最後的 prompt 就會進入互動模式：

```bash
uv run python frontier_knowledge.py
```

也可以用選項明確表示要進入互動模式：

```bash
uv run python frontier_knowledge.py --interactive
```

`--interactive` 不能和單次 prompt 同時使用。兩者一起提供時，程式會直接顯示錯誤，不會默默忽略其中一個。

## 互動模式的四個判斷

### 1. 空白輸入直接回到提示

使用者可能不小心只按下 Enter。這種輸入沒有問題內容，程式直接等待下一次輸入，不送出空的 HTTP 請求。

### 2. 用固定命令離開

目前接受三個退出命令：`exit`、`quit` 和 `:q`。判斷前會去除前後空白，英文字母不分大小寫；例如 ` EXIT ` 也會結束互動模式。

### 3. 單次錯誤不結束整個 runner

本地 runtime 沒啟動、port 錯誤或回傳格式不符時，`call_local_model()` 會回報 `RuntimeError`。互動迴圈把錯誤印到 stderr，接著回到輸入提示；修正 runtime 或網址後，可以直接繼續測試，不必重啟 runner。

### 4. Ctrl-D 和 Ctrl-C 都能結束

在 macOS 終端機按下 Ctrl-D 會送出 EOF（輸入結束訊號）；Ctrl-C 會觸發中斷。程式會把兩種情況都轉成結束訊息，不印出 Python traceback。

## 實作重點

互動流程集中在 `run_interactive()`。每次通過輸入與退出判斷後，才呼叫既有的 `call_local_model()`：

```python
while True:
    try:
        prompt = input("你 > ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n已結束本次互動。")
        return 0

    if not prompt:
        continue
    if prompt.casefold() in EXIT_COMMANDS:
        print("已結束本次互動。")
        return 0

    try:
        answer = call_local_model(...)
    except RuntimeError as error:
        print(f"錯誤：{error}", file=sys.stderr)
        continue

    print(f"模型 > {answer}")
```

每次請求只送出目前這一個 user message。畫面會保留先前的回答，但下一次 HTTP payload（送出的請求內容）不會帶上它們。今天先讓每個請求保持獨立，不把對話歷史混進來。

## 執行方式

先啟動 Day 2 使用的本地 runtime：

```bash
uv run mlx_lm.server \
  --model mlx-community/Llama-3.2-3B-Instruct-4bit \
  --port 8081
```

再在另一個終端機執行互動模式：

```bash
uv run python frontier_knowledge.py --interactive
```

輸入問題後，畫面會以 `模型 >` 開頭列出回答；接著可以輸入下一題，輸入 `:q` 結束。

如果 runtime 改用其他 port，單次模式和互動模式都加上同一個 `--base-url`：

```bash
uv run python frontier_knowledge.py \
  --interactive \
  --base-url http://127.0.0.1:8091/v1
```

## 本次檢查結果

先確認 Python 版本和 CLI 說明：

```text
./.venv/bin/python --version
Python 3.13.15

./.venv/bin/python frontier_knowledge.py --help
usage: frontier_knowledge.py [-h] [--interactive] [--base-url BASE_URL]
                             [--model MODEL] [--temperature TEMPERATURE]
                             [--max-tokens MAX_TOKENS]
                             [prompt]
```

輸入 `exit`，確認互動模式能正常結束：

```text
已進入互動模式。輸入 exit、quit 或 :q 結束。
你 > 已結束本次互動。
```

接著用 stub 回應（測試時替代真實服務的固定回應）取代 HTTP 回應。測試中間插入一次空白輸入，確認空白不會送出請求；兩個有效問題都能取得回答：

```text
interactive runner smoke test ok
requests: ['第一個問題', '第二個問題']
```

錯誤恢復測試則讓第一個請求回傳連線錯誤，第二個請求回傳測試答案。結果顯示，錯誤會印到 stderr，runner 仍能處理下一題：

```text
error recovery smoke test ok
```

這兩組 stub 測試只驗證 runner 的迴圈與輸入判斷，不代表本地模型的回答品質。前一次檢查時，執行環境沒有可用的 Metal device，所以無法啟動 `mlx_lm.server`。後續改用可以存取 Metal 的本機執行方式，先確認 `/v1/models` 列出目標模型：

```text
mlx-community/Llama-3.2-3B-Instruct-4bit
```

接著使用 Day 3 的互動命令送出兩個問題，再輸入 `:q`：

```bash
printf '請用一句話說明今天 Day 3 的目標。\n本地 runtime 在這個流程中負責什麼？\n:q\n' \
  | ./.venv/bin/python frontier_knowledge.py \
      --interactive \
      --base-url http://127.0.0.1:8081/v1
```

實際輸出如下：

```text
已進入互動模式。輸入 exit、quit 或 :q 結束。
你 > 模型 > 今天 Day 3 的目標是持續努力和推進，讓每一天都充滿著新意義和成長的機會。
你 > 模型 > I don't have enough information to provide a specific answer. Can you please provide more context or clarify which "流程" (process) you are referring to? I'll do my best to help.
你 > 已結束本次互動。
```

兩個請求都取得 HTTP 200，runner 以 exit code 0 結束。第二題的回答顯示模型沒有充分理解問題，但這不影響本次測試的目的：確認兩次請求、輸出與退出流程都能完成。這兩個回答不作為品質評估。

最後再跑一次 Day 2 的單次入口，確認互動模式加入後，原本的呼叫仍然成功：

```text
./.venv/bin/python frontier_knowledge.py --base-url http://127.0.0.1:8081/v1 "請只回答：單次模式正常。"
是的。
```

Day 2 的本地服務結果仍保留在 Day 2 文章。

## 今天的完成條件

- [x] 省略 prompt 時可以進入互動模式。
- [x] 互動模式可以連續處理多個問題。
- [x] 空白輸入不會產生模型請求。
- [x] `exit`、`quit` 和 `:q` 可以正常結束。
- [x] Ctrl-D 和 Ctrl-C 有明確的結束路徑。
- [x] 單次 prompt 的 Day 2 命令仍然保留。
- [x] 沒有新增第三方 Python 套件。
- [x] 在可用 Metal device 的本機執行兩題真實模型測試。

## 今天的取捨

今天完成的是一個可以重複提問、但不保存對話歷史的 CLI。每題只送出當下輸入，讓每次請求的 payload 保持清楚，也避免記憶體和輸入長度隨對話增加。

## 參考資料

- Day 2 文章
- [MLX-LM server 文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
