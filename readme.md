##AI 知識庫聊天系統（RAG 專案）

一個結合 PDF 文件檢索 + 本地中文 LLM 的問答系統，專案特色：可上傳 PDF 建立知識庫，使用 Ollama LLM 生成條理清楚、精簡的中文回答。

##功能概覽
1.PDF 上傳：支援上傳 PDF，或使用預設 PDF (test.pdf)
2.文件切割：使用 CharacterTextSplitter 將文件切成小段落
3.向量資料庫：透過 HuggingFaceEmbeddings + Chroma 建立向量搜尋
4.中文問答：使用本地 LLM Ollama (llama3) 回答問題
5.FastAPI 提供 API：/upload 上傳文件、/ask 提問問題

##技術架構
