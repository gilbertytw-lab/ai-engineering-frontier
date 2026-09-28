 # AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 12：同一個問題，三種資料搜尋路徑的差異在哪裡？

Day 10 做完 SQLite FTS5，系統可以從 11 個 chunks 找到關鍵字。Day 11 又補上 source catalog，讓五份 `harbor-api` 文件有了可以瀏覽的入口。

今天要比較三種搜尋路徑： raw、wiki、hierarchical，哪一種比較能精準符合使用者需求？

raw、wiki 在先前文章已經提過，而 hierarchical 指的是 **Hierarchical RAG （階層式 RAG）**，第一層先看 wiki、文件名稱、metadata 找出可能相關的文件，第二層再回到 raw 取出真正能支撐答案的 chunks。

## 三條路徑，其實是不同的 RAG 形式

我們先用資料流表示：

```text
A. Direct RAG
   raw documents → chunks → retrieval → answer

B. Wiki RAG
   wiki pages → retrieval → answer

C. Hierarchical RAG
   metadata/source pages → raw evidence chunks → answer
```

Direct RAG 直接在 raw 文件切出的 chunks 上搜尋。Day 10 的 SQLite FTS5 就是這條路徑目前的起點。

Wiki RAG 先把人類整理過的頁面當成搜尋資料。這條路徑很直覺：頁面比較短、標題比較好讀，模型也比較不需要面對整份原始文件。但它有一個前提，wiki 頁面真的要保存足夠的回答內容。

Hierarchical RAG（階層式檢索增強生成）多了一層選擇。先從 source catalog 或其他 metadata 找到可能相關的文件，再回到 raw chunks 取證據。翻成白話文就是：**wiki 負責帶路，raw 負責作證**。

這句話是今天比較的核心。

## 先用兩個固定查詢，不急著跑模型

我沿用目前資料集裡的工程問題，先跑兩個查詢：

```text
release owner
production release
```

第一個查詢比較窄，第二個查詢會同時碰到 release policy、deployment guide 和 service configuration。它們剛好可以看出精準查找和跨文件查找的差別。

查詢 `release owner`：

```text
建立 knowledge/index/retrieval.sqlite：5 份文件、11 個 chunks
查詢：release owner
命中 1 個 chunks
1. release-policy.md（第 12–29 行，bm25=3.229500，doc-3a8e2b68f2b171e3-chunk-0001）
```

這個結果很乾淨。答案在 `release-policy.md` 的同一個 chunk 裡，還保留了 raw 行號和 `chunk_id`。目前的 raw 路徑已經足以支撐一次精準回查。

查詢 `production release`，結果就開始變寬：命中 5 個 chunks，來自 3 份文件。五段 evidence 的 token 數合計 547，包含：

- `release-policy.md`：2 個 chunks，共 234 tokens。
- `deployment-guide.md`：2 個 chunks，共 267 tokens。
- `service-config.md`：1 個 chunk，共 46 tokens。

最後一份設定文件不是完全無關，它提到 production 設定變更需要 release record；但如果問題只是「production release 前要檢查什麼」，它比較像旁支證據，不該和 deployment checklist 享有同樣優先權。

## Wiki 很適合帶路，還不能單獨回答問題

Day 11 的 `knowledge/wiki/index.md` 目前列出 5 份 source pages。每一頁保存文件名稱、`document_id`、raw 路徑、source snapshot 和 hash；它沒有複製 raw 正文。

這個設計讓 source catalog 很適合回答：

- 現在有哪些文件？
- `release-policy.md` 對應哪個 `document_id`？
- 原始內容放在哪裡？
- 這一頁是由哪個 converter 版本產生的？

但它不適合直接回答：

- release owner 必須確認哪些事項？
- production 要先放量多少？
- rollback 的條件是什麼？

因為這些答案根本不在 source page 裡。若把 wiki 當成完整資料庫，結果會很像拿圖書館目錄回答書中的內容：書名和書架位置都對，答案還是在書裡。

## Hierarchical 路徑多做一步，反而比較省 tokens

把 `production release` 的結果拿來看，source catalog 可以先把候選範圍縮到 `release-policy.md` 和 `deployment-guide.md`。接著再回 raw 取這兩份文件的 chunks。

按照目前已經產生的 manifest 和 FTS 結果，這樣會得到 4 個 raw chunks，合計 501 tokens。接著我把三條路徑都交給同一個本機 Qwen，使用同一個問題、`temperature=0`、`enable_thinking=false` 和 `max_tokens=256`。

| 路徑 | 輸入內容 | evidence tokens | input tokens | 本次耗時 | 回答結果 |
|---|---|---:|---:|---:|---|
| raw 直接搜尋 | 3 份文件、5 個 chunks | 547 | 833 | 69.4 秒 | 列出 4 項 checks |
| wiki 直接回答 | 3 個 source pages | 1,199 | 1,378 | 76.5 秒 | 不知道 |
| hierarchical | 2 份文件、4 個 chunks | 501 | 762 | 94.1 秒 | 列出 4 項 checks |

這張表裡的 `wiki` evidence tokens 是三個 source page 本身的 token 數，不是 raw 證據；source page 沒有複製正文，卻仍然會佔用模型輸入空間。Hierarchical 則先用 metadata 選出兩份文件，再送回 raw chunks，所以從 5 個 chunks、547 tokens 降到 4 個 chunks、501 tokens。

省下的不是天文數字。這也不是證明階層式檢索一定比較準。

這次 live case 支持一個小但有用的判斷：在 context 有限的本地模型上，先縮小文件範圍，再取 raw evidence，有機會少送一點不必要的內容，而且仍然保留來源定位。

## Qwen 實際回答了什麼？

raw 和 hierarchical 兩條路徑都列出同一組 Required checks：CI 與 image tag／release ID 一致、staging 健康檢查和測試工作成功、production canary 觀察 15 分鐘，以及 release record 填入 rollback 目標。

wiki 路徑則明確回答不知道，原因很直接：它拿到的 source page 只有 `document_id`、raw path、hash 和連結，沒有 `release-policy.md` 的正文。它沒有把目錄內容猜成答案，這正是我們希望看到的拒答行為。

這次的本機 server 是用下面的命令啟動：

```bash
uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

延遲數字要保守看。這裡每條路徑只跑一次，順序是 raw、wiki、hierarchical；沒有足夠樣本控制模型快取、server 排程和其他本機負載。因此我把它當成這次請求的紀錄，不把 69.4、76.5 或 94.1 秒寫成路徑的固定速度。

今天能確定的範圍是：

- raw 路徑已經可以回傳可定位的候選 chunks。
- wiki source catalog 可以提供文件層導覽，但目前不包含回答所需的 raw 正文。
- hierarchical 路徑可以把導覽和證據分工，並在現有資料上形成較窄的候選範圍。
- 在同一個固定案例裡，raw 和 hierarchical 能拿到完整 Required checks，wiki 會拒答。
- 這只是一個 live case；要比較 retrieval recall、citation correctness 和平均延遲，仍然需要固定題目集與重複量測。

## 今天留下的判斷標準

到目前為止，我們可以把三層檢索過程定義清楚：

```text
wiki / metadata：我該去哪裡找？
raw chunks：原文到底寫了什麼？
LLM：如何根據這些資料組成回答？
```

只要回答需要引用原文、行號或 hash，最終 evidence 就不能只停在 wiki source page。wiki 可以做入口，也可以在之後增加 concept 或 howto 頁面；但整理頁越像答案，越需要保留它和 raw 證據之間的連結。

下一篇會把今天看到的 547 tokens 問題變成程式規則：固定 system prompt、保留 output reserve，對相鄰 chunks 去重，超過預算就停止加入證據。

## 參考資料

- [Day 10：資料分段後的查詢手法](day10.md)
- [Day 11：知識庫不能只是關鍵字搜尋](day11.md)
- [Knowledge files](../knowledge/README.md)
- [設計決策紀錄](../docs/design-decisions.md)
