# Day 7 驗證與編輯紀錄

查證日期：2026-09-21（Asia/Taipei）。本紀錄與文章分開，避免把編輯工作流混入教學正文。

## 實作與範圍

- 新增 `--checkpoint`，對真實 runtime 發出兩個 chat-completions request。
- 第一輪必須通過 Day 5 JSON 驗證，且內容恰好為 `{"answer": "收到", "limitations": []}`。
- 第一輪通過後才寫入 history；第二輪必須從 history 回答 `{"answer": "港口 17", "limitations": []}`。
- Checkpoint 固定 `temperature=0` 與 `json_answer=True`，但保留 `--base-url`、`--model`、`--system-prompt` 與 `--max-tokens` 設定。
- 任一 request、JSON 驗證或內容判定失敗時，命令回傳結束碼 1。
- 不把 checkpoint `PASS` 解釋成真實工程回答正確、長對話可用或跨 process 記憶。
- 沒有 commit、push 或發布。

## 自動驗證

執行環境：Python 3.13.15、mlx-lm 0.31.3、macOS Apple Silicon。

執行命令：

```bash
.venv/bin/python -m py_compile frontier_knowledge.py tests/test_day07.py
.venv/bin/python frontier_knowledge.py --help
.venv/bin/python -m unittest discover -s tests -v
```

結果：語法檢查與 CLI help 成功；18 項 unittest 全數通過。Day 7 新增 5 項 checkpoint 測試，Day 5 的 8 項與 Day 6 的 5 項全數保留。

Day 7 測試覆蓋：

1. 成功路徑固定使用 JSON，並在第二輪帶入第一輪完整回答。
2. 第一輪內容沒有按約定回答時失敗。
3. 第二輪沒有回答正確代號時失敗。
4. `call_local_model()` 失敗時回傳結束碼 1。
5. `--checkpoint` 與 prompt、`--interactive`、`--no-system-prompt`、`--json-answer` 或 `--no-history` 的衝突選項會由 CLI 拒絕。

## 真實模型驗證

使用現有快取並禁止下載啟動 server：

```bash
HF_HUB_OFFLINE=1 .venv/bin/python -m mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit --port 8081
```

這個啟動入口在 mlx-lm 0.31.3 顯示已淘汰警告，文章對讀者提供的命令維持 `uv run mlx_lm.server ...`。本次驗證的 server 只綁定 `127.0.0.1:8081`，並在驗證結束後以 `Ctrl+C` 關閉。

執行 checkpoint：

```bash
.venv/bin/python frontier_knowledge.py \
  --checkpoint \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024
```

完整 stdout：

```text
Checkpoint 1/2：單次 JSON 回答通過（answer=收到）
Checkpoint 2/2：Session history 回答通過（answer=港口 17）
Day 7 checkpoint：PASS
```

命令結束碼是 0。Server log 記錄兩個 `POST /v1/chat/completions` 均回傳 HTTP 200。

## 測試與主張邊界

| 主張 | 依據 | 邊界 |
| --- | --- | --- |
| Checkpoint 第一輪同時使用 system message 與 JSON 規則 | `run_checkpoint()` 的參數與 `test_checkpoint_reuses_first_structured_answer` | 沒有證明模型會對所有 prompt 遵守 system message |
| Checkpoint 第二輪帶入第一輪的 user／assistant message | 第二次 `call_local_model()` 的 history 測試 | 只驗證一組短對話 |
| Qwen 在本次實測回答正確代號 | 實際 stdout、結束碼 0 與兩個 HTTP 200 | 單次執行，不是模型品質 benchmark |
| 回答格式與任務內容都受到判定 | `parse_answer()` 與兩個完整 dict 比對 | 任務內容只檢查「收到」與「港口 17」 |
| 失敗可由 shell 觀察 | 失敗測試與 `run_checkpoint()` 的 return 1 | 沒有建立 CI workflow |

## 標題與副標備選

1. 第一週交付前，先讓 Chat Runner 自己跑完一次驗收｜用兩個 request 串起 JSON 與 Session history（電子報）。
2. 如何驗收一個本地 Chat Runner？｜Day 7 建立可重複執行的 checkpoint（SEO）。
3. 18 項測試通過還不夠｜再用真實 Qwen 串起第一週功能（社群）。
4. JSON 格式對了，對話也真的記得嗎？｜本地 Chat Runner 的端到端測試（社群）。
5. Day 7 第一週 checkpoint｜一條命令驗收 system message、JSON 與對話歷史（SEO）。

## 風格配方紀錄

教學實作型｜Simon 實證筆記風味｜深文｜單稿。開場回顧 Day 6 後直接提出整合驗收缺口；主體以可重現命令、實際 stdout、測試數量與主張邊界組成證據鏈。不虛構作者經歷，不另做雙稿；Day 7 本身是既定 30 天系列的週期 checkpoint，不另提拆篇建議。

pipeline：speak-human-tw（detect-first，blog）✓。首輪找到 2 處，經使用者確認後全數套用；保留文章的實測數字、命令、技術判斷與邊界說明。

自評：直接性 9／節奏 9／信任度 9／真實性 9／精煉度 9，共 45／50。這是編輯自評，不是外部評分。
