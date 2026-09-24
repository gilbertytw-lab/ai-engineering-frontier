# Day 9 驗證與編輯紀錄

查證日期：2026-09-23（Asia/Taipei）。本文與驗證紀錄分開，避免把 benchmark 的限制藏在教學正文後面。

## 實作與範圍

- `knowledge/ingest.py` 讀取 `knowledge/raw/*.md`，使用 Qwen tokenizer 以行邊界優先切分，建立 deterministic `knowledge/index/manifest.json`。
- manifest 保存 `document_id`、source metadata、raw SHA-256、chunk ID、raw 行號、token count、chunk text SHA-256 和正文；不覆寫 raw。
- 本次以 `--max-tokens 160 --overlap-tokens 24` 處理 Day 8 的五份 raw，產生 11 個 chunks。
- `knowledge/measure.py` 可先 dry run 計算 input tokens，也可呼叫 `frontier_knowledge.call_local_model()` 測量延遲。
- `call_local_model()` 新增可選的 `chat_template_kwargs`；既有呼叫若不傳此欄位，payload 行為不變。
- 量測命令預設關閉 Qwen thinking，明確比較可交付回答的輸入與延遲；用 `--enable-thinking` 可改測 reasoning 路徑。

## 自動驗證

執行環境：macOS 26.6.2 Apple Silicon、Python 3.13.15、`mlx-lm 0.31.3`。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24

HF_HUB_OFFLINE=1 uv run python knowledge/measure.py \
  --dry-run --evidence-tokens 160 320 640

uv run python -m unittest discover -s tests -v
git diff --check
```

結果：ingest 產生 5 份文件、11 個 chunks；dry run 得到 324、542、831 input tokens；27 項 unittest 通過；`git diff --check` 通過。

manifest 重建兩次後以完整 JSON 比對，內容相同。測試使用 fake tokenizer 驗證 chunk 邊界，不把 mock token 數當成 Qwen 實測數字。

## Dry run 證據

```text
{"evidence_tokens": 146, "input_tokens": 324, "requested_evidence_tokens": 160}
{"evidence_tokens": 314, "input_tokens": 542, "requested_evidence_tokens": 320}
{"evidence_tokens": 548, "input_tokens": 831, "requested_evidence_tokens": 640}
```

實際 evidence tokens 低於 requested budget，是因為選擇完整 chunk，下一個 chunk 放入後會超過該段預算，所以停止，不切半個 chunk 來湊數。

## 真實 Qwen 量測

使用現有本機快取並禁止下載：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

量測命令：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/measure.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 128 \
  --evidence-tokens 160 320 640 \
  --question 'production release 前，最少要檢查哪些事項？如果資料不足，請明確說不知道。'
```

命令以 `enable_thinking=false` 發送三個 request，完整重要欄位如下：

| requested evidence | evidence tokens | input tokens | elapsed_ms | output token estimate |
|---:|---:|---:|---:|---:|
| 160 | 146 | 324 | 23,710.2 | 112 |
| 320 | 314 | 542 | 27,303.4 | 128 |
| 640 | 548 | 831 | 29,298.6 | 128 |

三筆結果的 `status` 都是 `ok`。第二、三筆 output token estimate 到達 `max_tokens=128`，因此這不是完整回答長度的量測，也不能用來比較回答品質。

第一次沒有關閉 thinking 的請求在 `max_tokens=128` 時只回傳 `message.reasoning`，沒有 `message.content`；`knowledge/measure.py` 將它判定為失敗。這個結果保留在文章中作為實作邊界，不算入三筆成功量測。

本次三筆延遲是單一 server process、單一固定問題、單機單次結果。它支持「本環境中輸入變長時延遲上升」的觀察，不支持跨機器、跨模型或多次統計的效能保證。server 已在量測完成後以 `Ctrl+C` 關閉。

## 主張與依據

| 主張 | 依據 | 邊界 |
|---|---|---|
| raw 可建立可重建的 chunk manifest | `test_manifest_is_deterministic_and_keeps_source_location`、兩次實際 ingest 的完整 JSON 比對 | manifest 仍依賴 raw 檔存在；沒有測試刪除 raw 後還原 |
| chunk 不超過設定 token 上限 | ingest 單元測試與實際 11 個 chunks 的 token count | 超長單行以 tokenizer decode 重建片段，需再用實際文件型態補充測試 |
| input tokens 包含 system、問題、證據與 chat template | `Tokenizer.chat_count()` 與 dry run 輸出 | 實際 runtime 可能因 tokenizer／template 版本不同而改變 |
| Qwen 在三種輸入長度完成可讀回答 | 三筆 `status=ok`、HTTP 200 與 `answer_preview` | `max_tokens=128`；第二、三筆回答可能被截斷 |
| 證據不足時模型本次回答不知道 | 第一筆 answer preview 與固定問題要求 | 單次樣本，不是 no-answer 準確率 |
| 輸入變長時本次延遲上升 | 23.7／27.3／29.3 秒實測 | 沒有重複樣本、沒有統計信賴區間，也未控制 GPU cache 的所有狀態 |

## 標題與副標備選

1. 文件切多大，模型才吃得下？｜Day 9 用 tokenizer 和實測數字建立本機 context 預算（電子報）。
2. 如何替 raw Markdown 建立可重建 chunk manifest｜用來源行號、token count 和 hash 守住證據位置（SEO）。
3. context 不要用規格表猜｜Qwen 輸入從 324 到 831 tokens 的三次實測（社群）。
4. 先量再塞：本地知識庫的第一個 context budget｜從文件分段到問答延遲（SEO）。

## 風格配方紀錄

實測筆記型｜Simon 實證筆記風味｜深文｜單稿。沿用系列的回顧接棒、可重現命令、原始輸出與限制聲明；不虛構個人經歷，保留第一次量測失敗作為實作證據。

`blog-writing-zh` 技術檢查：操作型描述補上前置條件、命令、預期輸出與邊界；概念釐清補上 token、chunk、input token 與 evidence budget 的差異。系列評估：不拆篇，Day 9 只有一條主張，拆開會破壞從 ingest 到量測的遞進。

`speak-human-tw` detect-first 語感檢查：0 處需提出改寫。保留「不是量測器太挑剔」這類對失敗結果的直接判斷，沒有把必要的技術限制改成口號或廣告語。

自評：直接性 9／節奏 9／信任度 10／真實性 9／精煉度 9，共 46／50。這是編輯自評，不是外部評分。
