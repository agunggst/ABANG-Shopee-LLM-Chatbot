import streamlit as st
from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize MongoDB Client
uri = "mongodb+srv://wajemonstudio:rahasia123@wajemon.okrzgyr.mongodb.net/"
client = MongoClient(uri, tls=True)
collection = client['shopee']['answer_vec']

# Initialize Vector Store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorStore = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name="vector_index"
)

# Prompt Template
base_prompt = (
    "Your name is ABANG (Asisten Bot Andalan Ngomongin e-commerce). "
    "You work as a customer service representative at Shopee, a leading e-commerce in Indonesia. "
    "Your responsibility is to give accurate answers to customer questions. "
    "All responses should be in Indonesian and based on data that was already given. "
    "Your responses should be polite, professional, and helpful. "
    "Don’t answer to any questions or inquiries that are not related to Shopee. "
    "And do not explain any application outside Shopee."
)

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=base_prompt + "\n\nContext:\n{context}\n\nPertanyaan: {question}\nJawaban:"
)

# LLMs
llm_zephyr = HuggingFaceHub(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    huggingfacehub_api_token=huggingfacehub_api_token,
    model_kwargs={'temperature': 0.7, 'max_new_tokens': 256}
)

llm_gpt = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=openai_api_key,
    temperature=0,
    max_tokens=512
)


# Streamlit UI
st.set_page_config(page_title="ABANG Chatbot", page_icon="🤖")
st.title("🤖 ABANG - Asisten Bot Andalan Ngomongin e-commerce")
st.write("Tanyakan apa pun tentang Shopee. ABANG siap membantu kamu!")

# Model Selection
model_option = st.selectbox("Choose a Model:", ["Abang 1 (HuggingFaceH4/zephyr-7b-beta)",
                                                "Abang 2 (gpt-3.5-turbo)"])

if model_option == "Abang 1 (HuggingFaceH4/zephyr-7b-beta)":
    selected_llm = llm_zephyr
else:
    selected_llm = llm_gpt

# Input pertanyaan
question = st.text_input("Pertanyaan kamu:")

# On Submit
if st.button("Get answer"):
    if question.strip() == "":
        st.warning("Silakan masukkan pertanyaan.")
    else:
        qa_chain = RetrievalQA.from_chain_type(
            llm=selected_llm,
            chain_type='stuff',
            retriever=vectorStore.as_retriever(
                search_type='similarity',
                search_kwargs={'k': 3}
            ),
            chain_type_kwargs={'prompt': prompt_template}
        )

        response = qa_chain.invoke({"query": question})
        st.markdown(f"**Jawaban:** {response['result']}")

