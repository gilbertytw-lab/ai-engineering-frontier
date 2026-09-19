# Day 5 驗證與編輯紀錄

查證日期：2026-09-19（Asia/Taipei）。本紀錄與文章分開，避免把編輯工作流混入教學正文。

## 實作與範圍

- 延續既有 Day 4 未提交變更，新增 `--json-answer`；未改動 Day 4 文章。
- `parse_answer()` 驗證最外層物件、精確欄位、非空白字串與字串陣列，拒絕重複欄位與非標準數值常數。
- 採提示詞加生成後驗證；沒有傳送 `response_format`，沒有宣稱受限解碼。
- 一般文字模式保留；兩種模式都拒絕缺少、非字串或空白 `message.content`。
- 沒有新增依賴，沒有 commit、push 或發布。

## 驗證證據

執行環境：Python 3.13.15、mlx-lm 0.31.3、macOS Apple Silicon。

執行命令：

```bash
.venv/bin/python -m py_compile frontier_knowledge.py
.venv/bin/python frontier_knowledge.py --help
.venv/bin/python -m unittest discover -s tests -v
```

結果：語法檢查與 CLI help 成功；8 項 unittest 通過，其中一項包含 16 種不合格輸入。測試檔是 `tests/test_day05.py`，HTTP 層使用 mock，不能作為模型輸出品質證據。

真實模型服務以現有快取啟動，禁止下載：

```bash
HF_HUB_OFFLINE=1 .venv/bin/python -m mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit --port 8081
```

真實推論命令：

```bash
.venv/bin/python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --temperature 0.2 --max-tokens 1024 --json-answer \
  '請用 JSON 說明 system message 和 user message 的差別。answer 請用一句話，沒有限制時 limitations 使用空陣列。'
```

結束碼：0。驗證通過後的完整 stdout 已逐字保存在文章「再做一次真實模型互動」的小節。模型回答 system message 用於設定角色、行為與全局規則，user message 是具體問題或指令；`limitations` 為空陣列。本次只有一題真實推論；互動模式與錯誤路徑由 mock 測試驗證，沒有宣稱模型格式成功率。

文章以 `uv run` 提供既有專案的讀者入口；此次直接使用相同專案 `.venv/bin/python`，避免驗證時改動依賴。

## 主張與依據

| 主張 | 依據 | 邊界 |
| --- | --- | --- |
| JSON object、array、string 對應 dict、list、str | Python 3.13 官方 json 文件 | 不包含專案欄位規格 |
| 預設解析器接受重複欄位與 NaN 等擴充 | 官方相容性章節及本專案測試 | 專案另行拒絕 |
| system 指令接在原規則後，未送 response_format | `test_payload_and_roundtrip` | 不代表所有 runtime 都沒有相關能力 |
| 格式不合會失敗，互動模式會繼續 | unittest 的 CLI 與互動測試 | 使用固定回應，不是真實模型失敗率 |
| 正式模型可走完整條 JSON 路徑 | 本次實際 CLI 結束碼 0 與文章所載 stdout | 僅一個樣本 |
| schema 無法判斷答案真假 | 驗證器僅檢查結構、欄位及型別 | limitations 的語意也未自動查核 |

外部來源由 ego-browser task space 13 讀取官方原文後關閉。MLX-LM 網頁是 main 版文件；本機行為以已安裝 0.31.3 與實際命令為準。

## 標題與副標備選

1. 如何檢查本地模型的 JSON 回答｜從兩個欄位建立第一份 answer schema（SEO）。
2. 模型回了 JSON，就能放心接下去嗎？｜Day 5 實作欄位驗證與失敗處理（社群）。
3. 今天先拒收不合格式的回答｜把提示詞要求接上 Python 檢查（電子報）。

## 風格配方紀錄

教學實作／沿用系列自訂風格，以嚴謹教學的可重現性為主／深文／單稿。開場回顧 Day 4，接本日目標；不虛構作者經驗，不搬用其他作者人設；不新增系列拆篇建議。

套用 blog-writing-zh 的技術描述與來源檢查。指定的 speak-human-tw 承接語感檢查；本機沒有獨立 humanizer-zh skill，因此不宣稱執行該工具。

語感 detect-first 檢查結果：0 處需提出改寫。保留必要的操作步驟、錯誤訊息、測試數字、模型輸出與來源連結；不因列表或專有名詞而刪減技術資訊。未執行覆寫原稿的語感修訂。

自評：直接性 9／節奏 9／信任度 9／真實性 9／精煉度 9，共 45／50。這是編輯自評，不是外部評分。

已實際執行文章中的錯誤型別示範，輸出與文章一致。本次啟動的本地服務已在驗證結束後以 Ctrl+C 關閉。
