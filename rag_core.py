import os
import chromadb
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 1. Load env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 2. Set up models
groq_llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
Settings.llm = groq_llm
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# 3. Load documents
documents = SimpleDirectoryReader("data", recursive=True).load_data()
print(f"Loaded {len(documents)} documents")

# 4. Set up Chroma
chroma_client = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = chroma_client.get_or_create_collection("rag_kb")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 5. Build or load index
if chroma_collection.count() == 0:
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    print("Indexed documents for the first time")
else:
    index = VectorStoreIndex.from_vector_store(vector_store)
    print("Loaded existing index from Chroma")

# 6. Query
query_engine = index.as_query_engine(llm=groq_llm)
response = query_engine.query("How do I define a POST endpoint in FastAPI?")
print(response)