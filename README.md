# RAG Knowledge Base — Accelerator

## Problem
Companies store years of technical documentation across wikis, PDFs, and internal tools. Employees waste hours searching for answers that already exist.

## Solution
A natural language interface over any document collection. Ask a question, get a precise answer with context — no search, no digging.

## Who has this problem
Any software team with internal documentation: engineering wikis, API docs, onboarding guides, process documentation.

## Stack
- **LlamaIndex** — RAG orchestration
- **ChromaDB** — vector storage (local, persistent)
- **HuggingFace** — local embedding model (no API cost)
- **Groq + Llama 3.3** — LLM inference (free tier)
- **FastAPI** — REST API endpoint
- **Streamlit** — demo UI

## How to use

### 1. Clone and install
```bash
git clone https://github.com/alexcomandotme/rag-kb-poc.git
cd rag-kb-poc
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add your documents
Drop `.md`, `.txt`, or `.pdf` files into the `data/` folder.

### 3. Configure
```bash
cp .env.example .env
# Add your GROQ_API_KEY to .env
```

### 4. Index and run
```bash
python3 rag_core.py        # indexes documents into ChromaDB
uvicorn api:app --reload   # starts the API
streamlit run app.py       # starts the UI
```

## Reusability
Replace the `data/` folder with any document collection — internal wikis, contracts, HR policies, product specs. The pipeline is document-agnostic.

## PoC Summary
**Problem:** Technical knowledge is trapped in documents no one can find.  
**Solution:** RAG pipeline that indexes any document collection and answers natural language questions.  
**Stack:** LlamaIndex + ChromaDB + Groq + FastAPI + Streamlit.  
**Result:** Working demo in under a day, deployable as an internal tool or client PoC.