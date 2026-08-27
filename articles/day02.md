# Day 2：第一次在本機呼叫模型

日期：2026-08-27

今天把 Day 1 的環境基線往前推了一步：不再只確認版本，而是真的讓一個模型在本機回答問題。

這一天先不做聊天記憶、RAG 或 Agent。先把最小鏈路跑通，後面才知道每一層是在解決什麼問題。

## 先把三個名詞分開

這裡會同時看到模型、runtime 和程式，但它們不是同一件事。

- 模型是已經訓練好的參數檔案，負責根據輸入逐步產生下一段文字。
- runtime 是把模型載入記憶體、執行推論，並提供呼叫介面的服務。這次使用的 runtime 是 `mlx_lm.server`。
- `frontier_knowledge.py` 是我寫的呼叫端程式，負責把問題包成 HTTP 請求，送給 runtime，再把回答印出來。

「推論」在這裡指模型拿著已載入的參數，根據目前的輸入計算並產生回答；不是使用者自己在瀏覽器裡做的動作。

整條鏈路可以先縮成這樣：

```text
使用者輸入
    ↓
frontier_knowledge.py
    ↓ HTTP /v1/chat/completions
mlx_lm.server（本地 runtime）
    ↓
本地模型執行推論
    ↓
runtime 回傳 JSON
    ↓
frontier_knowledge.py 印出回答
```

目前還沒有知識庫。程式送進去的只有使用者這一次輸入，所以模型也不會自動知道我的文件內容。

## 為什麼先選這個 runtime

Day 1 確認這台電腦是 Apple Silicon。第一週只需要一個可以在本機載入模型、又能用 HTTP 介面呼叫的 runtime，因此先選 `mlx-lm`，不同時安裝多套推論框架。

這次使用的模型是：

```text
mlx-community/Llama-3.2-3B-Instruct-4bit
```

名稱裡的 `3B` 可以先理解成模型的參數規模；`4bit` 是較省記憶體的量化版本。它比較適合拿來做本機入門，但不代表回答品質、速度或可用的 context 長度一定符合需求，這些要留到後面的實測。

第一次執行會下載約 1.82 GB 的模型檔案。模型放在本機快取，不會被提交到 Git；這也是 `.tools/` 被加入 `.gitignore` 的原因之一。

## 建立 Python 3.13 環境

我沒有把系統的 Python 3.9.6 升級掉，也沒有讓專案直接依賴它。今天用 `uv` 建立專案自己的 Python 3.13 環境。

`uv` 在這裡同時幫忙建立隔離環境、解析 `pyproject.toml`，以及安裝套件。讀者已安裝 `uv` 後，在 Repository 根目錄執行：

```bash
uv venv --python 3.13
uv sync
```

專案用 `pyproject.toml` 宣告 Python 範圍與依賴，`.python-version` 則記錄主要版本線。這次實際驗證的版本是：

```text
Python 3.13.15
uv 0.12.6
mlx 0.32.2
mlx-lm 0.31.3
```

## 啟動本地 runtime

需要開兩個終端機。第一個終端機啟動服務：

```bash
uv run mlx_lm.server \
  --model mlx-community/Llama-3.2-3B-Instruct-4bit \
  --port 8080
```

這個指令會讓 runtime 在本機的 `8080` port 等待請求。它不是把模型變成雲端服務，網址仍然是 `127.0.0.1`，也就是這台電腦自己。

如果終端機顯示 `Address already in use`，代表 `8080` 已被其他程式使用。不要為了排除問題就直接結束不認識的 process；可以先換一個 port，例如 `8081`，然後讓呼叫端使用相同的網址。

本次測試的 `8080` 已被占用，所以我保留原 process，改用 `8081` 啟動 runtime。這個差異只影響網址，不影響程式設計。

## 寫一個最小呼叫端

第二個終端機執行：

```bash
uv run python frontier_knowledge.py \
  --base-url http://127.0.0.1:8080/v1 \
  "請用一句話說明本地模型和網頁聊天 AI 的差別。"
```

如果 runtime 使用 `8081`，只要把 `--base-url` 改成：

```text
http://127.0.0.1:8081/v1
```

`frontier_knowledge.py` 刻意只用 Python 標準函式庫的 `urllib`。Day 2 的重點是看懂請求怎麼從程式送到 runtime，不先增加一個 HTTP client 套件。

程式做的事情也只有幾步：

1. 把輸入放進 `messages`。
2. POST 到 `/chat/completions`。
3. 讀取回傳的 JSON。
4. 取出 `choices[0].message.content` 並印出。
5. 連不到服務或回傳格式不對時，顯示可理解的錯誤。

這個 API 的格式和 OpenAI Chat Completions 類似，但請求在這次實驗中只送到自己的電腦，不會因為使用相同格式就自動送往 OpenAI。

## 實際結果

我使用 `8081` 做了本次 smoke test。`/v1/models` 能列出模型後，再透過呼叫端送出問題，實際輸出如下：

```text
本地模型（Local Model）和網頁聊天 AI 的差別在於，本地模型可以直接在使用者端的電腦上執行，提供更快速和更私密的聊天體驗，而網頁聊天 AI 切換需要通過網頁伺服器
```

這代表三件事已經成立：

- Python 3.13 的隔離環境可以載入 `mlx-lm`。
- runtime 可以載入指定的本地模型。
- 呼叫端可以送出訊息並解析模型回覆。

但這不是回答品質測試。輸出中的「更快速」和「更私密」不能直接當成保證：實際速度受硬體、模型大小和設定影響，資料是否離開電腦也要看整個應用程式的資料流。Day 2 只驗證連線與基本資料格式，還沒有替回答內容背書。

## 今天留下的檔案

```text
pyproject.toml          專案版本與依賴
.python-version         Python 主要版本線
uv.lock                 已解析的依賴版本
frontier_knowledge.py   最小本地模型呼叫端
```

本次沒有把模型檔、虛擬環境或本機執行紀錄放進 Git。它們可以重新下載或重新建立，屬於衍生的本地產物。

## 今天的完成條件

- [x] 建立 Python 3.13.15 隔離環境。
- [x] 安裝並驗證 `mlx-lm`。
- [x] 啟動一個本地 OpenAI-compatible runtime。
- [x] 從自己的 Python 程式送出一次訊息。
- [x] 取得並印出本地模型回答。
- [x] 記錄 port 被占用時的處理方式。

## 還沒有做的事

現在每次執行都只處理一個問題，還沒有固定的 system prompt，也沒有保存對話歷史。這是刻意留下的空白：如果一開始就把聊天、記憶、文件和工具全部混進來，出了問題很難知道是哪一層造成的。

下一天會把這次的一次性呼叫整理成可重複使用的 Chat Runner，先讓「同一個 runtime 可以連續服務多次請求」變成清楚的程式責任。

## 參考資料

- [MLX-LM server 文件](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
- [MLX-LM 套件頁面](https://pypi.org/project/mlx-lm/)
- [uv 安裝文件](https://docs.astral.sh/uv/getting-started/installation/)
