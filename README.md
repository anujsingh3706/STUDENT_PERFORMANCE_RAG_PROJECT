# 🎓 Student Performance RAG Chatbot with Analytics Dashboard

## 🚀 Overview

This project is an **AI-powered Student Performance Analysis System** built using **Retrieval-Augmented Generation (RAG)**.

It allows users to:

* Ask natural language questions about student data 💬
* Get intelligent, context-aware responses 🧠
* Analyze performance using interactive dashboards 📊

---

## 🧠 Key Features

### 🔹 RAG-Based Chatbot

* Uses **LangChain** for building RAG pipeline
* Retrieves relevant student data using **FAISS vector database**
* Generates responses using **LLM (Groq - LLaMA 3)**

### 🔹 Conversation Memory

* Maintains chat history
* Enables context-aware conversations

### 🔹 Custom Dataset

* JSON dataset with **200+ student records**
* Includes:

  * Marks (5 subjects)
  * Attendance
  * Performance categories
  * Weak subjects

### 🔹 Analytics Dashboard

* Built using **Streamlit**
* Includes:

  * 📊 Marks distribution
  * 📈 Performance categories
  * 🔥 Attendance vs Marks correlation
* Filter by class and performance

---

## 🏗️ Project Architecture

```
User Query
   ↓
Streamlit UI
   ↓
RAG Pipeline (LangChain)
   ↓
Retriever (FAISS)
   ↓
Student Dataset (JSON)
   ↓
LLM (Groq - LLaMA 3)
   ↓
Final Response
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **FAISS (Vector Database)**
* **HuggingFace Embeddings (MiniLM)**
* **Groq API (LLaMA 3)**
* **Streamlit**
* **Pandas & Matplotlib**

---

## 📂 Project Structure

```
student-rag-chatbot/
│
├── app/
│   ├── main.py
│   ├── test_chat.py
│   ├── config.py
│
├── data/
│   ├── students.json
│
├── ingestion/
│   ├── loader.py
│   ├── splitter.py
│
├── embeddings/
│   ├── embedder.py
│
├── vectorstore/
│   ├── vectordb.py
│
├── rag/
│   ├── chain.py
│   ├── llm.py
│
├── memory/
│   ├── memory.py
│
├── dashboard/
│   ├── analytics.py
│
├── build_index.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/student-rag-chatbot.git
cd student-rag-chatbot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama3-8b-8192
```

---

## 📦 Build Vector Database

```bash
python build_index.py
```

---

## ▶️ Run Chatbot (CLI)

```bash
python -m app.test_chat
```

---

## 🌐 Run Web App

```bash
streamlit run app/main.py
```

---

## 💬 Sample Queries

* "Who are the top performing students?"
* "Which students are weak in Math?"
* "Show students with low attendance"
* "Compare student S001 and S010"
* "Give improvement suggestions for weak students"

---

## 📊 Dashboard Features

* Marks distribution histogram
* Performance category analysis
* Attendance vs marks visualization
* Dynamic filtering (class & performance)

---

## 🧠 How It Works (RAG Pipeline)

1. JSON data → converted to text documents
2. Documents → split into chunks
3. Chunks → converted into embeddings
4. Stored in FAISS vector database
5. User query → semantic search
6. Retrieved context → passed to LLM
7. LLM generates final answer

---

## 🚀 Deployment

The app can be deployed on:

* Streamlit Cloud
* Render
* HuggingFace Spaces

---

## 🔥 Future Improvements

* User authentication
* Upload custom datasets
* Advanced filtering & search
* PDF report generation
* Real-time database integration
* Voice-based interaction

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests.

---

## 📧 Contact

For queries or collaboration:

* GitHub: https://github.com/anujsingh3706

---

## ⭐ If you like this project, give it a star!
