# ABANG (*Asisten Bot Andalan Ngomongin e-commerce*)
---
## Team Members
- **Fajar Daud Khabibilah** *as Data Analyst*
- **Hafizal Shakur** *as Data Scientist*
- **I Gusti Agung Agastya Tarumawijaya** *as Data Engineer + Data Scientist*
- **Muhammad Iqbal** *as Data Scientist*

---
## Repository Outline

|File Name                | Explanation                                                               |
|-------------------------|---------------------------------------------------------------------------|
|data_scraping.ipynb      | File notebook berisikan syntax untuk melakukan data scraping              |
|shopee_qna_data_raw.csv  | Data hasil scraping                                                       |
|data_cleaning.ipynb      | File notebook untuk melakukan data cleaning                               |
|shopee_qna_data_clean.csv| Data setelah melalui proses cleaning                                      |
|eda.ipynb                | Notebook untuk melakukan eksplorasi data                                  |
|rag_vecdg.ipynb          | Notebook untuk menyimpan hasil embedding ke dalam NoSQL Database (MongoDB)|
|rag_query.ipynb          | File untuk melatih model LLM                                              |
|app.py                   | File deployment                                                           |

---
## Project Background
Di era modern saat ini, kebutuhan akan asisten dalam bentuk ai/chatbot pada platform e-commerce cukup tinggi. Keberadaan ai assistant/chatbot pada e-commerce bertujuan untuk memudahkan user dalam mengambil sebuah keputusan atau mendapatkan informasi yang diinginkan. Kelebihan lain dari kepemilikan chatbot pada sebuah e-commerce dapat menunjukan kredibilitas dari pengelola platform tersebut untuk memberikan pelayanan dasn pengalaman  kepada user menjadi lebih baik. Karena faktanya masih banyak user yang mengeluhkan kurang optimalnya servis yang diberikan dalam menjawab segala keresahan.

Untuk menghadapi masalah tersebut, dibutuhkan solusi yang dapat meminimalisir keluhan dari user mengenai pengalamanya dalam mengakses laman e-commerce dengan mengaplikasikan fitur chatbot ke dalamnya. Karena menurut [sumber](https://www.puskomedia.id/blog/chatbot-dalam-industri-e-commerce-dongkrak-dukungan-pelanggan-dan-tingkatkan-pengalaman-berbelanja/?utm_source=chatgpt.com), chatbot memiliki beberapa kelebihan yang dapat menigkatkan penjualan, memberikan pengalaman pada pelanggan, dan efisiensi biaya. Dengan inovasi seperti itu, dapat mempertahankan eksistensi sebuah platform e-commerce dan mampu bersaing dengan kompetitor lainnya.

---
## Objective
Dalam project kali ini, akan diciptakan sebuah chatbot berbasis LLM yang dirancang untuk membantu pelanggan e-commerce, khususnya pengguna Shopee, dalam menjawab berbagai permasalahan seputar Frequently Asked Questions (FAQ) pada platform tersebut. Chatbot ini mampu menjawab pertanyaan seputar konflik umum seperti penolakan paket dan pengembalian barang yang rusak. Data chatbot diperoleh melalui proses scraping informasi dan keluhan pengguna di platform Shopee.

---
## Dataset
Dataset yang digunakan didapatkan menggunakan metode scraping dengan bantuan library selenium dan bs4 bersumber dari halaman Help Center - [Shopee](https://help.shopee.co.id/portal/4/category).

---
## Stacks
- Programming Language  : **Python, JavaScript**
- Tools and Framewoks   : **MongoDB, VSCode, Streamlit, ReactJs, FastAPI** 
- Library               : **selenium, bs4, pandas, matplotlib, seaborn, mongoDB, langchain, streamlit, OpenAI, HuggingFace**

---
## Others
- [Google Slides](https://docs.google.com/presentation/d/1XtjErSc3UvQk-SgeatE9w11x-hybarJo8UVzzO7y8yc/edit#slide=id.p5)
- [Deployment 1](https://huggingface.co/spaces/mbale014/ABANG-chatbot-for-shopee)
- [Deployment 2](https://abang-shopeebot.web.app/)