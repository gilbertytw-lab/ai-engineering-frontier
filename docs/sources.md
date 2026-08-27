# 來源紀錄

這份文件只登錄實際使用或引用的外部資料。每筆來源都要說明用途；只讀過但沒有影響實作的資料，不直接改寫成文章內容。

## 登錄格式

```text
### SXXX：來源名稱
- URL：
- 存取日期：
- 用途：
- 使用範圍：
- 是否包含程式碼、文字或圖片：否／是（說明授權）
```

## Day 1

### S001：speak-human-tw

- URL：https://github.com/Raymondhou0917/speak-human-tw
- 使用的公開文件：README、`SKILL.md`、`references/patterns.md`、`references/humanize.md`、`references/taiwan-localization.md`
- 存取日期：2026-08-27
- 用途：整理本專案的繁體中文文章自查方向，降低公式化、空泛和翻譯腔。
- 使用範圍：只參考「先保事實、再處理語氣」的工作原則與台灣用語檢查方向；Day 1 文章由本專案重新撰寫。
- 是否包含程式碼、文字或圖片：否

Day 1 沒有把外部文章、程式碼、圖片或範例資料放入 Repository。後續若使用模型官方文件、套件文件或研究論文，會在實際使用前補登錄 URL、日期與用途。

### S002：Python 官方版本與支援狀態

- URL：https://devguide.python.org/versions/
- 存取日期：2026-08-27
- 用途：確認 Python 3.9 已結束支援，以及 3.12、3.13、3.14 的維護狀態。
- 使用範圍：只作為本專案版本策略的依據，不複製頁面內容。
- 是否包含程式碼、文字或圖片：否

### S003：MLX-LM 套件資訊

- URL：https://pypi.org/project/mlx-lm/
- 存取日期：2026-08-27
- 用途：確認 Apple Silicon 本地模型 runtime 的 Python 需求與安裝前提。
- 使用範圍：只作為 Day 2 runtime smoke test 的參考，不預先假設所有依賴都相容。
- 是否包含程式碼、文字或圖片：否

### S004：MLX-LM server 文件

- URL：https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
- 存取日期：2026-08-27
- 用途：確認本地 HTTP server 的啟動方式、模型參數與 OpenAI-compatible endpoint。
- 使用範圍：依文件重新組合 Day 2 的啟動命令與呼叫流程；沒有複製文章或專案結構。
- 是否包含程式碼、文字或圖片：否

### S005：uv 安裝文件

- URL：https://docs.astral.sh/uv/getting-started/installation/
- 存取日期：2026-08-27
- 用途：確認 uv 的安裝方式與 Python 環境管理命令。
- 使用範圍：只作為本機工具安裝與環境建立的參考；文章命令依本專案目錄與版本重新整理。
- 是否包含程式碼、文字或圖片：否
