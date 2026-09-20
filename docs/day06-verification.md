# Day 6 驗證與編輯紀錄

查證日期：2026-09-20（Asia/Taipei）。本紀錄與文章分開，避免把編輯工作流混入教學正文。

## 實作與範圍

- 互動模式預設保存同一次 Python process 內成功完成的 `user`／`assistant` 回合。
- `system` message 每次 request 只組裝一次，不存入 history。
- runtime 或回答驗證失敗時，該回合不寫入 history。
- 新增 `--no-history` 比較 Day 5 的獨立 request；單次 prompt 使用此選項時回報參數錯誤。
- 單次模式、文字模式與 `--json-answer` 保留，沒有新增依賴。
- history 沒有持久化、token 計算、截斷或摘要；沒有宣稱跨 process 記憶。
- 沒有 commit、push 或發布。

## 驗證證據

執行環境：Python 3.13.15、mlx-lm 0.31.3、macOS Apple Silicon。

執行命令：

```bash
.venv/bin/python -m py_compile frontier_knowledge.py
.venv/bin/python frontier_knowledge.py --help
.venv/bin/python -m unittest discover -s tests -v
```

結果：語法檢查與 CLI help 成功；13 項 unittest 通過。Day 6 新增 5 項 Session history 測試，Day 5 的 8 項測試全數保留。

真實模型服務使用現有快取並禁止下載：

```bash
HF_HUB_OFFLINE=1 .venv/bin/python -m mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit --port 8081
```

history 開啟時的測試命令：

```bash
printf '%s\n' \
  '請記住代號「港口 17」，只回答「收到」。' \
  '上一題的代號是什麼？只回答代號。' \
  'exit' | .venv/bin/python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --temperature 0 --max-tokens 1024 --interactive
```

完整 stdout：

```text
已進入互動模式。輸入 exit、quit 或 :q 結束。
你 > 模型 >

收到
你 > 模型 >

港口 17
你 > 已結束本次互動。
```

history 關閉時使用相同輸入，命令只多一個 `--no-history`。完整 stdout：

```text
已進入互動模式。輸入 exit、quit 或 :q 結束。
你 > 模型 >

收到
你 > 模型 >

不知道。
你 > 已結束本次互動。
```

兩次命令結束碼都是 0。輸出在回答前包含空白行，來源是本次模型回傳內容；文章為可讀性省略空白行，沒有改動回答文字。

本次啟動的 server 已在驗證結束後以 `Ctrl+C` 關閉。

MLX-LM server 官方文件已於同日重新開啟核對。文件說明 HTTP API 的設計接近 OpenAI chat API，`messages` 是代表 conversation history 的 message object 陣列；本篇只引用這項介面事實。實際行為仍以本機 mlx-lm 0.31.3、payload 測試與真實推論為準。

## 測試與主張邊界

| 主張 | 依據 | 邊界 |
| --- | --- | --- |
| 第二輪 payload 依序包含第一輪的問題與回答 | `test_interactive_reuses_successful_turns` 與 `test_build_messages_places_history_between_system_and_current_user` | 測試 HTTP 呼叫前的 Python 資料，不代表模型一定善用前文 |
| 失敗回合不進入 history | `test_failed_turn_is_not_added_to_history` | 只涵蓋 `call_local_model()` 丟出 `RuntimeError` 的路徑 |
| `--no-history` 維持各輪獨立 | `test_no_history_keeps_requests_independent` | system message 仍會出現在每次 request |
| Qwen 能在本次 history 測試答出代號 | 實際 CLI stdout 與結束碼 0 | 單一問題、單次執行，不代表長對話品質 |
| 關閉 history 後，本次 Qwen 回答不知道 | 實際 CLI stdout 與結束碼 0 | 這是行為對照，模型輸出仍可能隨版本與取樣改變 |
| Session 結束後不保留對話 | history 只存在 `run_interactive()` 的區域變數 | 沒有測試跨 process 儲存，因為本日沒有實作持久化 |

## 標題與副標備選

1. 如何替本地 Chat Runner 加上對話記憶｜用 `messages` 保存 Session history（SEO）。
2. 模型真的記得上一題嗎？｜Day 6 拆開聊天畫面與 request payload（社群）。
3. 這次答對，因為前文真的有送出去｜本地互動模式的 Session history 實作（電子報）。
4. 解密多輪對話：每一輪都重新送出哪些訊息？｜從 payload 看懂本地模型的短期記憶（SEO）。

## 風格配方紀錄

教學實作／沿用系列自訂風格，以嚴謹教學的可重現性為主／深文／單稿。開場回顧 Day 5，接本日缺口；使用操作型主體，補上 context 成本與非持久化邊界。不虛構作者經驗，不搬用其他作者人設；Day 6 是既定 30 天系列的一篇，不另做拆篇建議。

套用 blog-writing-zh 的技術描述與來源檢查。指定的 speak-human-tw 以部落格中等力度完成 detect-first 語感檢查，結果為 0 處需提出改寫；沒有為了增加口語感而改動技術敘述。

自評：直接性 9／節奏 9／信任度 9／真實性 9／精煉度 9，共 45／50。這是編輯自評，不是外部評分。
