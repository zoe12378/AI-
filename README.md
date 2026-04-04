# 🚀 AI 知識庫聊天系統  
### 📚 PDF × 向量搜尋 × 本地 LLM（Ollama）

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/LangChain-RAG-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Vector%20DB-Chroma-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/LLM-Ollama-black?style=for-the-badge">
</p>

---

## ✨ 專案介紹

這是一個使用 **Python + FastAPI** 建立的 AI 知識庫聊天系統。  
使用者可以上傳 PDF 文件，系統會自動解析內容並建立向量資料庫，最後透過 **本地 LLM（Ollama）** 回答問題。

本專案實作了完整的 **RAG（Retrieval-Augmented Generation）架構**，讓 AI 回答具備依據，而不是憑空生成。

---

## 🔥 專案亮點（面試重點）

- ✅ 使用本地 LLM（Ollama），不依賴雲端 API  
- ✅ 完整實作 RAG 架構（文件 → 向量 → 問答）  
- ✅ 支援 PDF 上傳並自動建立知識庫  
- ✅ 使用語意搜尋提升回答準確度  
- ✅ 前後端整合，具備實際操作介面  

---

## 🧠 系統架構

```mermaid
graph TD
A[上傳 PDF] --> B[文件切割]
B --> C[文字向量化]
C --> D[Chroma 向量資料庫]

E[使用者提問] --> F[相似度搜尋]
F --> D
D --> G[取出相關內容]
G --> H[Ollama LLM]
H --> I[生成回答]
