# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 4：Prompt 到底改變了什麼？先從 system message 開始

Day 3 把一次性呼叫改成互動式 Chat Runner。程式可以連續接收問題，但每次 request 只送出目前那一題，模型看不到前面的對話。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 從 Day 4 開始固定使用 Qwen3.8

Day 1 曾把 Qwen3.8-27B 列為 target model 與硬體規劃背景；但 Day 1 到 Day 3 只先示範環境建立、HTTP 呼叫與互動式 CLI 等基礎功能。從今天開始，正式專案統一使用 `mlx-community/Qwen3.8-27B-4bit`，前 3 天的示範模型不代表正式專案的模型選型。

這個切換是刻意的：先用較小的模型把資料流和程式邊界驗證清楚，再從 Day 4 開始用正式模型觀察 system message 與後續功能。

今天先不處理對話記憶，也不急著做 JSON 格式。只在送出 user prompt 之前，加上一條固定的 system message，觀察請求內容和模型行為各自改變了什麼。

## 今天要完成的目標

- 每次請求都預設加入一則 `system` message。
- 保留 Day 3 的單次模式和互動模式。
- 用 `--no-system-prompt` 回到 Day 3 的請求格式，方便做基線比較。
- 用 `--system-prompt` 暫時替換預設規則。
- 實際確認本地 runtime 可以接受這個 `messages` payload。

本篇難度以 Level 1 為主：照著做可以看到結果。想修改自己的回答規則，可以進到 Level 2；想改寫請求組裝邏輯，則是 Level 3。

## 先把兩種 message 分開

Day 3 的請求只有一則訊息：

```json
{
  "messages": [
    {"role": "user", "content": "請說明本地模型是什麼。"}
  ]
}
```

Day 4 在前面加上一則固定規則：

```json
{
  "messages": [
    {
      "role": "system",
      "content": "你是本地工程知識助理。請用繁體中文直接回答問題，先給結論，再補充必要說明。資訊不足時，請明確說明不知道，不要自行捏造。"
    },
    {"role": "user", "content": "請說明本地模型是什麼。"}
  ]
}
```

`user` message 是這一輪實際提出的問題；`system` message 則是送出問題時一併提供的固定工作規則。MLX-LM server 收到 chat request 後，會把這些 message 交給模型的 chat template 處理；細節可以對照 [MLX-LM server 文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md) 和 [目前的 server 實作](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/server.py)。

這裡有一個很容易誤會的地方：system message 是輸入內容的一部分。它可以影響模型，但不等於程式層級的強制驗證，也不會自動阻止模型胡說。今天先把它當成「固定放在每一題前面的工作說明」，這個心智模型比較準確。

## 今天改了哪些程式

### 1. 加入預設 system prompt

`frontier_knowledge.py` 現在有一個 `DEFAULT_SYSTEM_PROMPT`：

```python
DEFAULT_SYSTEM_PROMPT = (
    "你是本地工程知識助理。請用繁體中文直接回答問題，先給結論，再補充必要說明。"
    "資訊不足時，請明確說明不知道，不要自行捏造。"
)
```

這段文字是本專案自己寫的工作規則，不是模型的內建知識。後面如果要調整回答風格，會先改這個入口，再觀察輸出是否真的改變。

### 2. 把組裝 messages 的工作獨立出來

程式新增 `build_messages()`，依序建立 `system` 和 `user`：

```python
def build_messages(prompt: str, system_prompt: str | None) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    return messages
```

這個函式目前很小，卻把 Day 4 的變更集中在一個地方。單次模式和互動模式都呼叫同一個 `call_local_model()`，所以兩種入口會使用相同的 system prompt。

### 3. 保留比較用的兩個選項

不加任何選項時，使用預設 system prompt：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  "請說明這個 runner 今天多了什麼能力？"
```

想回到 Day 3 的單一 `user` message，可以明確停用：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --no-system-prompt \
  "請說明這個 runner 今天多了什麼能力？"
```

也可以在不改程式的情況下換一條規則：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --system-prompt "請用三個條列說明，資訊不足時請回答不知道。" \
  "本地 runtime 今天新增了什麼？"
```

`--system-prompt` 和 `--no-system-prompt` 不能同時使用。互動模式也沿用同一條規則：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --interactive
```

輸入兩個問題時，每一個 request 都會帶著 system prompt，但 Day 3 的限制仍然存在：前一題的問題和回答不會自動附加到下一題。

## 跟著做一次完整測試

先開啟第一個終端機，啟動正式專案使用的本地 runtime：

```bash
uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

再開第二個終端機，先檢查模型服務是否已經回應：

```bash
curl http://127.0.0.1:8081/v1/models
```

回應中應該能找到你啟動的模型名稱：

```text
mlx-community/Qwen3.8-27B-4bit
```

目前 runtime 可能同時列出其他已可用的模型，因此重點是確認回應中包含這個 Qwen3.8 model ID；呼叫端也會用 `--model` 明確指定它。

Qwen3.8 會先產生 reasoning，再產生 `message.content`。本次驗證發現，`--max-tokens 64` 和 `--max-tokens 256` 都可能在 content 出現前耗盡上限，讓呼叫端判定回應格式不完整；以下範例固定使用 `1024`。

接著執行預設路徑：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  "請回答：今天的測試是否完成？請只用一句繁體中文回答。"
```

本次 Qwen3.8 實測輸出如下；模型輸出每次可能不同，不要把這段文字當成固定快照：

```text
我不知道今天的測試是否完成。
```

這個答案本身不是今天要評分的對象。這次測試要確認的是：程式成功把 system message 和 user prompt 一起送到本地 runtime，並取得合法的 chat completion。

### 再測客製規則

把 system prompt 換成一條很容易觀察的規則：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --system-prompt "只回答 SYSTEM_OK，不要補充其他文字。" \
  "請回答現在的時間。"
```

本次 Qwen3.8 實測輸出是：

```text
我不知道現在的時間。
```

這個結果反而值得留下來。模型沒有完整照做，代表 system prompt 不是硬限制；它仍可能受到模型本身、chat template、取樣設定和 user prompt 影響。若文章把 system prompt 寫成「一定遵守的規則」，讀者之後一定會在某個案例踩到坑。

### 關掉 system prompt 做基線比較

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --no-system-prompt \
  "請回答：今天的測試是否完成？請只用一句繁體中文回答。"
```

本次 Qwen3.8 實測輸出是：

```text
我無法確認今天的測試是否完成。
```

兩次回答都可能因為模型取樣而改變，所以比較的重點放在 request payload，不放在單次文字輸出。要研究 system prompt 的效果，至少要固定模型、temperature、max tokens、問題和測試次數，之後再談品質差異。

## 我怎麼驗證這次改動

先做不需要啟動模型的檢查：

```bash
./.venv/bin/python -m py_compile frontier_knowledge.py
./.venv/bin/python frontier_knowledge.py --help
```

接著用固定回應的 stub 取代 HTTP 回應，檢查程式實際送出的 JSON。預期結果如下：

```text
day04 payload smoke test ok
messages[0].role = system
messages[1].role = user
without system = only user message
```

完成上述步驟後，我用真正的本地 MLX-LM server 和 `mlx-community/Qwen3.8-27B-4bit` 完成三條路徑：預設 system prompt、客製 system prompt、`--no-system-prompt`。`/v1/models` 回應中包含 Qwen3.8 model ID，三條 CLI 路徑都成功取得 `message.content`。本篇記錄的是這次驗證結果，不把單次回答當成固定結果，因為輸出會受到模型、temperature、max tokens 和其他生成設定影響。

這裡要把驗證範圍說清楚。今天確認的是請求組裝、HTTP 連線、回應解析和三種 CLI 入口；還沒有用固定資料集評估回答品質，也沒有證明模型一定遵守 system prompt。這些問題留到後面的 schema 與 evaluation 再處理。

## 今天的完成條件

- [x] 預設請求包含一則 `system` message。
- [x] `user` prompt 仍然是最後一則輸入訊息。
- [x] 單次模式可以使用預設規則。
- [x] 互動模式可以使用預設規則。
- [x] `--no-system-prompt` 可以回到 Day 3 的請求格式。
- [x] `--system-prompt` 可以替換預設規則。
- [x] 本地 runtime 成功處理三種路徑。
- [x] 沒有新增 Python 套件。

## 今天的取捨

今天只加入一層固定指令，沒有把回答強行解析成 JSON，也沒有保存對話歷史。這樣可以單獨觀察 system message 的作用；下一步再處理「回答長什麼樣子」，比較不會把多個變更混在同一次測試裡。

Day 4 的程式知道如何把規則送進 request，還不知道如何驗證模型有沒有照做。這兩件事中間，差了一個很大的洞。

下一篇會補上回答 schema，讓程式至少能檢查模型回傳的結構，而不是只把一段文字原封不動印出來。

## 參考資料

- [Day 3 文章](day03.md)
- [MLX-LM server 文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
- [MLX-LM server 實作](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/server.py)
- [uv 安裝文件](https://docs.astral.sh/uv/getting-started/installation/)
