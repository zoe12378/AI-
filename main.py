from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
import os

app = FastAPI()

# 允許跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vectorstore = None
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = Ollama(model="llama3")

@app.get("/")
def get_index():
    return FileResponse("index.html")

DEFAULT_PDF = "test.pdf"
if os.path.exists(DEFAULT_PDF):
    loader = PyPDFLoader(DEFAULT_PDF)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_split = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(docs_split, embeddings)
    print(f"✅ 已讀取預設 PDF：{DEFAULT_PDF}")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    global vectorstore
    contents = await file.read()
    temp_path = "temp.pdf"
    with open(temp_path, "wb") as f:
        f.write(contents)

    loader = PyPDFLoader(temp_path)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_split = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(docs_split, embeddings)

    return JSONResponse({"status": "success", "message": f"✅ 文件 {file.filename} 已處理完成"})

@app.get("/ask")
def ask(query: str):
    global vectorstore
    if vectorstore is None:
        return JSONResponse({"status": "error", "message": "❌ 請先上傳文件"})

    docs = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
你是一位專業的中文助理。
請用繁體中文回答以下問題，條理清楚、段落分明，避免英文。
請把以下文章內容用繁體中文簡短摘要成大概三四句話，只保留核心概念：
{context}

【問題】:{query}
"""
    answer = llm.invoke(prompt)
    return JSONResponse({"query": query, "answer": answer})