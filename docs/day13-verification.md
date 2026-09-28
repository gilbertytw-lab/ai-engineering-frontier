# Day 13 驗證與編輯紀錄

查證日期：2026-09-25（Asia/Taipei）。本文與驗證紀錄分開，避免把 context budget 的設計限制藏在教學正文後面。

## 實作與範圍

- `knowledge/context.py` 從既有 SQLite FTS5 結果組裝受限的 context。
- 預算先扣除 system prompt、問題、對話歷史、工具 schema 與 output reserve，再決定可以放入多少證據。
- 同一份文件的重疊行號只保留排名較前的 chunk；每個被淘汰的候選都保存原因。
- 最終使用同一個 Qwen tokenizer 的 `chat_count()` 計算實際 message token，而不是只加總 raw chunk 的 `token_count`。
- 本日沒有啟動 Qwen；只驗證候選排序、去重、預算截斷和 message 組裝。

## 實際命令

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/context.py \
  --query 'production release' \
  --question 'production release 前，最少要檢查哪些事項？如果資料不足，請明確說不知道。' \
  --limit 5 \
  --context-window 1024 \
  --output-reserve 128
```

輸出：

```text
候選 5 個；去重後選入 4 個，淘汰 1 個
base input tokens=124，retrieval budget=772，final input tokens=723，output reserve=128
1. release-policy.md（第 12–29 行，doc-3a8e2b68f2b171e3-chunk-0001）
2. deployment-guide.md（第 12–24 行，doc-891dc9cf617077c2-chunk-0001）
3. deployment-guide.md（第 25–33 行，doc-891dc9cf617077c2-chunk-0002）
4. service-config.md（第 32–35 行，doc-3317e1a5be5eb33f-chunk-0003）
淘汰：doc-3a8e2b68f2b171e3-chunk-0002（overlapping_lines_with:doc-3a8e2b68f2b171e3-chunk-0001）
```

`final input tokens + output reserve = 851`，低於本次指定的 `context_window=1024`。這個 1,024 是本次可重跑的 request cap，不是模型規格宣稱的最大 context。

## 自動化測試

```bash
uv run python -m unittest tests.test_day13_context -v
uv run python -m unittest discover -s tests -v
git diff --check
```

結果：Day 13 測試 3 項通過；全專案測試 38 項通過；`git diff --check` 通過。

測試涵蓋：

- 相同文件的重疊行號會保留較高排名的候選，真正相鄰且沒有重疊的 chunks 仍可同時保留。
- history 與 tool schema 會被算進 base input tokens。
- 超過 output reserve 後的候選會被拒絕，並留下 `context_budget` 原因。
- 候選輸入順序改變時，排序和選入結果仍然一致。

## 已知限制

- 去重依賴同一文件的行號重疊和文字 hash，不做語意相似度判斷。
- CLI 使用既有的 `retrieval.sqlite`；它仍然是 Day 10 的 lexical retriever，不會因為 context builder 出現就獲得同義詞搜尋能力。
- 本次只做 message 組裝，尚未把結果交給 Qwen，也尚未產生 citation 或 no-answer 評估。
- `context_window=1024` 與 `output_reserve=128` 是本次驗證設定，之後仍要用不同問題集和 runtime 量測重新校準。

## 標題與副標備選

1. Context budget 不只是數字：Day 13 開始管理證據進場順序｜從 5 個候選 chunks 到 4 個可追溯證據（SEO）。
2. 為什麼檢索到的 chunks 不能全部送進模型？｜用 system prompt、output reserve 和重疊去重組出 bounded context（電子報）。
3. 讓有限 context 用在刀口上｜本地 RAG 如何記錄選入與淘汰的每一段證據（社群）。
4. Day 13：先扣掉模型要說的話，剩下的才是證據空間｜一次看懂 context builder 的預算公式（SEO）。

## 風格配方紀錄

教學實作型｜Simon 實證筆記風味｜深文｜單稿。沿用系列的回顧接棒、可重現命令、輸出證據和限制聲明；不虛構本機 Qwen 回答，明確區分 context 組裝驗證和模型實測。

`blog-writing-zh` 技術檢查：以操作型描述說明前置條件、命令、預期輸出和副作用；以概念釐清說明 raw chunk token、chat input token、retrieval budget 和 output reserve 的差異。系列評估：不拆篇，Day 13 的單一主張是「context 必須成為可計算、可回查的選擇規則」。

`speak-human-tw` detect-first 語感檢查：0 處需提出改寫。保留技術限制、單句急停和直接判斷，沒有加入不存在的個人經歷或泛用口號。

自評：直接性 9／節奏 9／信任度 10／真實性 9／精煉度 9，共 46／50。這是編輯自評，不是外部評分。
