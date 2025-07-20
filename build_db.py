from sentence_transformers import SentenceTransformer
import chromadb
from preprocess import chunks
import chromadb
import os

CHROMA_DB_DIR = os.path.abspath("chroma_db")
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.create_collection("knowledge_base")

for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk.page_content).tolist()
    collection.add(
        embeddings=[embedding],
        documents=[chunk.page_content],
        metadatas=[{"id": i}],
        ids=[str(i)]
    )

print("Database built successfully with", len(chunks), "chunks.")
