from fastapi import FastAPI, Request
from pydantic import BaseModel
from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# --- Load ENV ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_DB_PASS = os.getenv("MONGO_DB_PASS")

# --- Init API ---
app = FastAPI()

# --- CORS config ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Setup MongoDB & Embeddings ---
uri = f"mongodb+srv://wajemonstudio:{MONGO_DB_PASS}@wajemon.okrzgyr.mongodb.net/"
client = MongoClient(uri, tls=True)
collection = client['shopee']['answer_vec']

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = MongoDBAtlasVectorSearch(collection, embedding, index_name='vector_index')

# --- Prompt Template ---
base_prompt = "Your name is ABANG (Asisten Bot Andalan Ngomongin e-commerce), You work as a customer service representative at Shopee, a leading e-commerce in Indonesia. Your responsibility is to give accurate answers to customer questions. All responses should be in Indonesian and based on data that was already given. Your responses should be polite, professional, and helpful. Don’t answer to any questions or inquiries that are not related to Shopee. And do not explain any application outside shopee"

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template= base_prompt + "\n\nContext:\n{context}\n\nPertanyaan: {question}\nJawaban:"
)

# --- LLM GPT 3.5 ---
llm_gpt = ChatOpenAI(model="gpt-3.5-turbo",
                 openai_api_key=OPENAI_API_KEY,
                 temperature=0, max_tokens=512)

qa_gpt = RetrievalQA.from_chain_type(
    llm=llm_gpt,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
    chain_type_kwargs={"prompt": prompt_template}
)

# --- API Request Schema ---
class QuestionInput(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(data: QuestionInput):
    result = qa_gpt.run(data.question)
    return {"answer": result}