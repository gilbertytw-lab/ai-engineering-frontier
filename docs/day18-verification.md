# Day 18 驗證紀錄

驗證日期：2026-10-02（Asia/Taipei）。

文章：[Day 18：我用 10 題檢查 Qwen 會不會選對工具](../articles/day18.md)

## 評估範圍

- 使用 `knowledge/routing_cases.json` 的 10 個預先標記案例，涵蓋四個工具、不呼叫工具、只讀取候選標題，以及先搜尋、等使用者選擇的界線。
- `knowledge/evaluate_routing.py` 使用既有 system prompt 與 tool schemas，每題只呼叫模型一次，擷取第一個工具選擇。
- 評分比對工具名稱或「不呼叫工具」。arguments 會記錄，但不評分；工具函式、網路搜尋、文件讀取、來源匯入和索引重建都不會執行。
- 搜尋結果案例使用 `example.org` fixture，不連線至外部網站。

## 執行方式

啟動本地 MLX-LM server 後執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/evaluate_routing.py
```

模型：`mlx-community/Qwen3.8-27B-4bit`；temperature：0；每題一個模型請求。

## 結果

```text
case_count=10
completed_count=10
error_count=0
correct_count=10
exact_match_rate=1.0
false_tool_count=0
missed_tool_count=0
wrong_tool_count=0
```

平均單題耗時約 6.2 秒，最短 2.7 秒，最長 11.8 秒。記錄包含 prompt cache 暖機，不做跨機器效能比較。

逐題 JSONL 記錄位於 Git 忽略的 `runs/day18-routing-20261002-180631.jsonl`。

## 限制

這是單一模型、單次執行、10 個人工設計案例的路由檢查。它不代表一般化的路由準確率，也沒有評估 arguments 是否符合工具 schema、工具執行結果或最終回答品質。

## 文章配方與語感檢查

教學實作型｜Simon 實證筆記風味｜標準｜單稿。`speak-human-tw` detect-first 檢查：0 處待修。

目前環境沒有 `humanizer-zh`，未執行 blog-writing-zh 的下游檢查。接續檢查可用：「請用 humanizer-zh 以 detect 模式、technical voice 檢查 `articles/day18.md`，只列 AI 寫作痕跡，不要改字；保留 Qwen 10 題評估結果、實測限制、工具選擇與不執行工具的邊界。」
