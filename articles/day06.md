# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 6：模型真的記得上一題嗎？把對話歷史放回每次 request

Day 05 已經能要求模型回傳固定 JSON，互動模式卻還有一個很明顯的缺口：終端機看起來像在聊天，模型每次實際收到的只有當下那一題。前一輪問過什麼、模型答過什麼，都留在終端機畫面上，沒有進入下一次 request。

今天把 Session history 接起來。完成後，同一次互動期間的成功回合會依序放回 `messages`；程式結束後，歷史也跟著消失。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## Day05 的互動模式少了什麼？

假設連續輸入兩句：

```text
請記住代號「港口 17」，只回答「收到」。
上一題的代號是什麼？只回答代號。
```

Day 05 會送出兩個互相獨立的 request。第二次 payload 裡只有固定規則和「上一題的代號是什麼？」；「港口 17」從來沒有送進去。模型若答對，只能算猜中，不能算記得。

Day 06 改成在 Python 程式裡保留已完成的回合。第二次 request 的 `messages` 會長成這樣：

```json
[
  {"role": "system", "content": "固定的回答規則"},
  {"role": "user", "content": "請記住代號「港口 17」，只回答「收到」。"},
  {"role": "assistant", "content": "收到"},
  {"role": "user", "content": "上一題的代號是什麼？只回答代號。"}
]
```

這裡的「記憶」很樸素：呼叫端把舊訊息重新送一次。模型服務不需要替這個 CLI 保存使用者的 Session，也不會在下一個全新 request 自動想起前文。

## 今天改了哪些程式

### `build_messages()` 接受 history

原本的 `build_messages()` 只組裝 `system` 和目前的 `user` message。現在多收一份 `history`，排列順序固定為：

```text
system
過去的 user / assistant 回合
目前的 user message
```

```python
def build_messages(
    prompt: str,
    system_prompt: str | None,
    history: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": prompt})
    return messages
```

`system` message 仍然只出現一次。若每一輪都把它追加到 history，規則會在 payload 中重複，之後也更難計算 context。

### 只保存成功完成的回合

`run_interactive()` 啟動時建立空的 `history`。每次呼叫成功後，再加入這一輪的問題與回答：

```python
history.extend(
    [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": answer},
    ]
)
```

若 runtime 連線失敗，或 Day 05 的 JSON 驗證沒有通過，這一輪不會寫進歷史。下一題因此不會帶著一筆「有問題、沒答案」的半套回合繼續跑。

送出請求時使用 `history.copy()`。這份淺拷貝記錄的是當下的訊息順序，也避免呼叫端拿到同一個之後還會持續變長的 list。

### 保留 Day05 的比較路徑

互動模式現在預設開啟 history。想確認差異時，可以加上 `--no-history`，讓每一題恢復成獨立 request：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --temperature 0 \
  --max-tokens 1024 \
  --interactive --no-history
```

`--no-history` 只適用於互動模式。單次 prompt 本來就沒有前一輪可保留，若把兩者一起使用，CLI 會直接回報參數錯誤。

## 跟著做一次對照測試

先啟動本地 runtime：

```bash
uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

再開另一個終端機，進入互動模式：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --temperature 0 \
  --max-tokens 1024 \
  --interactive
```

依序輸入：

```text
請記住代號「港口 17」，只回答「收到」。
上一題的代號是什麼？只回答代號。
```

本次使用 Qwen3.8-27B-4bit 的輸出是：

```text
模型 > 收到
模型 > 港口 17
```

接著重新啟動 Runner，命令加上 `--no-history`，輸入相同兩句。本次輸出變成：

```text
模型 > 收到
模型 > 不知道。
```

單次生成仍可能受模型與取樣影響。這組結果提供了可觀察的行為差異；真正能證明程式有沒有夾帶歷史的，仍是 request payload 測試。

## 自動測試檢查什麼

Day 06 新增 5 項測試：

- history 位於 `system` 與目前問題之間。
- 第二輪能收到第一輪成功完成的 `user`／`assistant` 訊息。
- 呼叫失敗的回合不會寫入 history。
- `--no-history` 讓各輪 request 維持獨立。
- 單次 prompt 不接受 `--no-history`。

加上 Day 05 的 8 項回歸測試，目前共 13 項：

```bash
uv run python -m unittest discover -s tests -v
```

本次執行結果是 13 項全部通過。JSON 回答模式、文字模式和原本的錯誤處理仍保留。

## Session history 的代價

第二輪會重送第一輪，第三輪又會重送前兩輪。對話愈長，輸入內容就愈多，延遲和 context 使用量也會跟著增加。目前程式沒有計算 tokens、截斷舊訊息或摘要歷史，因此不適合無限制地聊下去。

這份 history 也沒有寫入檔案或資料庫。輸入 `exit`、按下 `Ctrl+C`，或重新啟動程式後，上一個 Session 就不存在了。它和 Day 26 預計處理的可重設 Session State 還有一段距離。

現在先守住一條邊界：Day 06 只證明「後一題能看到前一輪」。等後面真的要把文件證據塞進 prompt，再一起處理 context budget、去重與截斷。

## 今天留下什麼

今天增加了記憶體內的 Session history，解決互動模式看似連續、request 實際互不相干的問題。可以執行的命令是：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --interactive
```

Day 07 會把第一週的 Runner 整理成可獨立執行的 checkpoint，確認單次呼叫、system message、JSON schema 和 Session history 能一起工作。

## 參考資料

- [Day 5：讓模型回答固定 JSON 格式](day05.md)
- [MLX-LM server 官方文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
