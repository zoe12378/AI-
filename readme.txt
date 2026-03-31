# 🏛 朕的理財小能手 RAG 專案

這個專案是一個 **中文 PDF RAG 系統**，結合了文件檢索與本地生成式 AI (LLM)，可以將 PDF 內容做快速搜尋並生成條理清楚的中文摘要或回答。

## 📌 技術堆疊

- **Python**：核心語言
- **FastAPI**：建立 REST API
  - `/upload`：上傳 PDF 並建立向量資料庫
  - `/ask`：提問並由 LLM 回答
- **PDF 處理**：`PyPDFLoader` 載入 PDF，`CharacterTextSplitter` 分段
- **向量搜尋**：
  - `HuggingFaceEmbeddings` 將文字轉向量
  - `Chroma` 本地向量資料庫
- **本地 LLM**：
  - `Ollama + llama3` 生成中文回答
- **Prompt Engineering**：自訂 prompt 控制回答風格、繁體中文、精簡摘要

## 🛠 系統流程

1. PDF → 載入 → 切段 → embeddings → Chroma  
2. 使用者提問 → Chroma 相似度搜尋 → LLM 處理 → 回答  
3. FastAPI 提供 API 入口，支援即時互動

## 💡 功能亮點

- 支援 PDF 上傳與自動向量化
- 使用本地 LLM，無需雲端 API
- 中文條理清楚的摘要與回答
- 適合放入作品集展示 RAG 應用
