# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## 專案定位

這是一個以 **一般工程師與對 AI 有興趣的大眾也能跟得上** 為目標的 30 天 AI Engineering 實驗系列。

核心不是單純介紹 Prompt、RAG、Agent、MCP 等熱門名詞，而是固定使用同一套硬體與同一顆本地模型，逐步加入不同 AI Engineering 方法，實際觀察：

> **模型不換、硬體不換，AI Engineering 到底能讓它變強多少？**

整個系列會盡量避免變成「AI 名詞百科」，而是透過一個一個可以實際驗證的小問題，建立 AI Engineering 技術為什麼會出現、解決了什麼問題，以及它實際帶來多少改善的完整脈絡。

---

## 參賽主題

- 組別：AI Engineering
- 題目：**AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡**
- 核心主線：**固定模型、固定硬體，逐層加入 AI Engineering 能力**
- 實驗原則：Local-first、可重現、以實測取代純理論整理

---

## 實驗環境

### Hardware

- MacBook Air
- Apple Silicon
- 10-core CPU
- 32 GB Unified Memory
- 1 TB SSD

### Model

- Qwen3.8-27B-DFlash2

### 基本限制

整個系列盡量維持以下控制變因：

- 不更換主要模型
- 不使用雲端 GPU 作為主要運算來源
- 優先使用本地推論
- 同一批測試資料反覆使用
- 所有技術盡量建立可量化比較
- 所有實驗盡量能讓讀者自行重現

---

# 系列研究問題

整個 30 天系列主要回答一個問題：

> 如果模型本身完全沒有升級，只靠 AI Engineering，我們到底可以讓它變得多好？

技術演進主線：

```text
直接問模型
    ↓
Prompt
    ↓
Context
    ↓
Long Context
    ↓
Retrieval
    ↓
RAG
    ↓
Reranker
    ↓
Tool Calling
    ↓
MCP
    ↓
Agent
    ↓
Memory
    ↓
Agent Loop
    ↓
Evaluation
    ↓
Observability / Guardrail
```

但這條路線只作為背景。

每一天真正的核心都是：

> **今天我要驗證什麼？**

---

# 目標讀者

主要面向：

- 平常有使用 ChatGPT、Claude、Gemini 等 AI 工具的人
- 軟體工程師
- AI 初學者
- 想了解 Local LLM 的讀者
- 對 AI Agent、RAG、MCP 有興趣，但還沒有完整概念的人

預設讀者能力：

- 知道 LLM 是什麼
- 可以閱讀簡單 Python
- 不要求具備 Machine Learning 數學背景
- 不要求理解 Transformer 細節
- 不要求具備模型訓練經驗

---

# 難度設計原則

## 一篇只處理一個核心問題

避免一次介紹大量專有名詞。

例如介紹 RAG 時，不會第一篇就同時塞入：

- Embedding
- Vector Database
- Chunking
- HNSW
- Cosine Similarity
- Reranker
- Recall@K
- MRR

而會拆解成不同文章。

例如：

1. 為什麼不能把整份文件直接丟給 AI？
2. AI 怎麼知道哪段文字和問題最相關？
3. 找到相關資料後，為什麼還需要重新排序？

讓技術自然長出來。

---

# 每篇文章建議結構

每篇盡量固定使用以下格式：

## 1. 今天遇到什麼問題？

用一般人能理解的方式描述。

## 2. 為什麼原本的方法不夠？

先建立技術出現的需求。

## 3. 今天的新技術是什麼？

用直覺解釋概念。

## 4. 實際跑一次

使用固定 Mac + Qwen 模型實驗。

## 5. 結果

提供：

- 正確率
- Latency
- 記憶體
- Tokens/s
- 成功率

等可量化資料。

## 6. 一句話結論

讓一般讀者不用理解全部技術，也能知道實驗結果。

## 7. 下一個問題

把下一篇文章自然接上。

---

# 30 天文章規劃

## Week 1 — 先認識我們手上的 AI

### Day 1 — AI Engineering 到底是在 Engineering 什麼？

核心問題：

> 模型都訓練好了，為什麼還需要 Engineering？

內容方向：

- AI Model vs AI System
- AI Engineering 的角色
- 系列實驗規則
- 固定模型、固定硬體的原因

實驗：

建立第一版 Baseline。

---

### Day 2 — 32GB Mac 真的能跑 27B 模型嗎？

核心問題：

> 消費級 Mac 可以成為 AI 開發機嗎？

量測：

- RAM
- 啟動時間
- Tokens/s
- TTFT
- CPU / GPU 使用狀況

---

### Day 3 — 27B 到底代表什麼？

核心問題：

> 模型比較大就一定比較聰明嗎？

內容：

- Parameter 的直覺解釋
- 27B 的規模
- 模型大小與硬體需求

避免深入 Transformer 數學。

---

### Day 4 — Prompt 寫法真的會影響結果嗎？

實驗：

同一問題測：

- 短 Prompt
- 詳細 Prompt
- 結構化 Prompt

比較結果品質。

---

### Day 5 — System Prompt 到底改變了什麼？

實驗：

固定 User Prompt，只修改 System Prompt。

觀察：

- 回答格式
- 行為
- 穩定性

---

### Day 6 — AI 為什麼會忘記前面的事情？

介紹：

- Context Window
- Token
- Conversation History

實驗：

逐步增加 Context。

---

### Day 7 — Context 越多真的越好嗎？

實驗：

相同問題使用：

- 1K context
- 4K context
- 8K context
- 16K context
- 32K context

觀察：

- 正確率
- Latency
- Memory

第一週總結：

> 更多資訊不一定等於更好的答案。

---

# Week 2 — 讓 AI 開始會找資料

## Day 8 — 把整份文件丟給 AI 不就好了嗎？

比較：

Long Context vs Retrieval。

---

## Day 9 — AI 怎麼知道哪段文字跟問題有關？

介紹：

Embedding。

避免數學推導，以「語意座標」解釋。

---

## Day 10 — Vector Database 是什麼？

建立最小可用 Vector Search。

---

## Day 11 — 文件要切多大才好？

Chunk Size 實驗：

- 300
- 500
- 1000
- 2000

比較 Retrieval 效果。

---

## Day 12 — Top-K 越多越準嗎？

比較：

- Top 1
- Top 3
- Top 5
- Top 10

---

## Day 13 — RAG 到底是不是 AI 版開書考？

完整組出第一版 RAG。

比較：

```text
Baseline
vs
Long Context
vs
RAG
```

---

## Day 14 — 搜到資料還不夠：為什麼需要 Reranker？

加入 Reranker。

比較：

```text
RAG
vs
RAG + Reranker
```

第二週總結：

> AI 不需要記住所有東西，但需要知道去哪裡找。

---

# Week 3 — 讓 AI 開始會做事情

## Day 15 — AI 為什麼需要 Tool Calling？

核心問題：

> 知道答案和真的能做事情，是兩回事。

做第一個 Tool：

例如 Calculator。

---

## Day 16 — AI 怎麼知道該用哪個工具？

建立多工具環境。

例如：

- Calculator
- Search
- File Reader

觀察 Tool Selection。

---

## Day 17 — Tool Calling 會不會叫錯工具？

建立 Tool Calling Benchmark。

量測：

Tool selection accuracy。

---

## Day 18 — MCP 到底解決了什麼？

從「每個工具自己接」引出 MCP。

重點不是 MCP 規格，而是：

> 為什麼大家需要共同的工具介面？

---

## Day 19 — 做一個最小 MCP 實驗

建立簡單 MCP Server / Client。

---

## Day 20 — Tool Calling 和 Agent 差在哪？

比較：

```text
LLM
↓
LLM + Tool
↓
Agent
```

---

## Day 21 — Agent 到底是什麼？

建立最小 Agent Loop：

```text
Observe
↓
Think
↓
Act
↓
Observe
```

第三週總結：

> AI 從「回答問題」開始變成「執行任務」。

---

# Week 4 — AI 可以自己持續工作嗎？

## Day 22 — Agent 為什麼會失控？

測試：

- 重複呼叫工具
- 不必要步驟
- 無限 Loop
- 錯誤 Planning

---

## Day 23 — AI 需要記憶嗎？

比較：

- No Memory
- Conversation Memory
- External Memory

---

## Day 24 — Harness Engineering 是什麼？

討論：

模型外部到底需要多少工程？

包含：

- Prompt
- Tools
- Context
- Runtime
- State
- Validation

---

## Day 25 — Loop Engineering 是新東西還是新名字？

研究近年 Agent Loop 的概念。

核心問題：

> Agent 真正的能力，究竟來自模型，還是來自 Loop？

---

## Day 26 — 多想幾次真的會比較好嗎？

比較：

```text
Single Pass
vs
Retry
vs
Self-Reflection
```

---

## Day 27 — Verifier 可以讓 AI 自己改答案嗎？

建立：

```text
Generator
↓
Verifier
↓
Retry
```

觀察正確率是否提升。

---

# Week 5 — 最後三天：證明它真的變強了

## Day 28 — 「感覺比較好」不算工程：怎麼評估 AI？

介紹：

- Golden Dataset
- Accuracy
- Success Rate
- Latency
- Memory

建立固定 Benchmark。

---

## Day 29 — 30 天後，它到底變強多少？

完整比較：

| System | Accuracy | Latency | RAM | Tokens/s |
|---|---:|---:|---:|---:|
| Base LLM | | | | |
| + Prompt | | | | |
| + Context | | | | |
| + RAG | | | | |
| + Reranker | | | | |
| + Tools | | | | |
| + Agent | | | | |
| + Verification | | | | |

---

## Day 30 — 模型從來沒換過：AI Engineering 到底做了什麼？

最終回答：

> 模型沒有改變，但系統改變了多少？

整理：

- 最有效的 Engineering 技術
- 最不值得的 Engineering 方法
- Local AI 的限制
- 32GB Mac 的極限
- AI Engineering 真正的價值

最後留下完整 GitHub Repo。

---

# 統一 Benchmark 設計

建議所有重要實驗都記錄：

## Quality

- Accuracy
- Success Rate
- Hallucination Rate

## Performance

- TTFT
- Total Latency
- Tokens/s

## Resources

- Peak RAM
- Model Size
- Context Size

## Stability

同一題重複執行：

- 3 次
- 5 次
- 或 10 次

觀察結果變異。

---

# 系列最重要的控制變因

整個系列盡量維持：

```text
Same Hardware
Same Model
Same Dataset
Same Benchmark
```

只改：

```text
AI Engineering Method
```

因此最後才有辦法回答：

> 改善究竟是來自模型，還是來自工程？

---

# 如何降低撞題風險

本系列刻意避免以下方向：

- 30 天 AI 名詞介紹
- 30 天 RAG 教學
- 30 天 Agent 教學
- Prompt → Context → Agent 的純概念整理
- 單純閱讀 Paper 後摘要
- 每天介紹一個熱門 Framework

而是採用：

> **固定環境 + 控制變因 + 實際 Benchmark + 技術演進脈絡**

即使別人也寫：

- RAG
- MCP
- Agent
- Context Engineering

本系列仍然有明確區隔。

因為問題不是：

> RAG 是什麼？

而是：

> 在相同 27B 模型與 32GB Mac 上，RAG 是否真的比 Long Context 更有效？

---

# Repository 建議結構

```text
ai-engineering-frontier/
│
├── README.md
├── articles/
│   ├── day01.md
│   ├── day02.md
│   ├── ...
│   └── day30.md
│
├── experiments/
│   ├── baseline/
│   ├── prompt/
│   ├── context/
│   ├── rag/
│   ├── reranker/
│   ├── tools/
│   ├── mcp/
│   ├── agent/
│   └── evaluation/
│
├── benchmarks/
│   ├── dataset.json
│   ├── results/
│   └── README.md
│
├── scripts/
│
├── data/
│
├── docs/
│   ├── architecture/
│   └── notes/
│
└── requirements.txt
```

如果後續主要使用 MLX / uv / pyproject.toml，也可以再調整。

---

# Repo 最終成果

30 天完成後，Repository 不只是文章備份，而應該留下：

1. 30 篇完整文章
2. 一套固定 Benchmark
3. 一個 Baseline LLM
4. Long Context 實驗
5. Local RAG
6. Reranker
7. Tool Calling
8. MCP 實驗
9. Minimal Agent
10. Agent Loop
11. Verifier
12. 完整 Benchmark Results
13. 32GB Mac Local AI Engineering 報告

---

# GitHub Repository Name

## 首選

```text
ai-engineering-frontier
```

優點：

- 短
- 好記
- 和鐵人賽題目一致
- 未來鐵人賽結束後仍然可以持續維護
- 不綁定特定模型或 Mac

---

## 其他候選

```text
30-days-ai-engineering
```

比較直接，強調鐵人賽 30 天。

```text
local-ai-engineering-lab
```

更強調實驗室與 Local AI。

```text
ai-engineering-on-mac
```

更明確凸顯硬體特色，但未來延伸性稍弱。

```text
one-model-30-days
```

特色很強，但較不像正式技術 Repository。

---

# 建議 Repository Description

推薦版本：

> 30 days of practical AI Engineering experiments on a 32GB Mac — exploring how far one local LLM can go with context, RAG, tools, agents, loops and evaluation.

較適合中文讀者的版本：

> 30 天 AI Engineering 實驗：固定一台 32GB Mac 與一顆本地 LLM，實測 Context、RAG、Tools、Agent、Loop 與 Evaluation 能讓模型走多遠。

---

# 最推薦設定

Repository Name：

```text
ai-engineering-frontier
```

Description：

```text
30 days of practical AI Engineering experiments on a 32GB Mac — exploring how far one local LLM can go with context, RAG, tools, agents, loops and evaluation.
```

Series：

> **AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡**

Core Question：

> **模型不換、硬體不換，AI Engineering 到底能讓它變強多少？**
