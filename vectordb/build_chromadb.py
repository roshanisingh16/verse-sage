import json
import chromadb
import os
import shutil
from chromadb.utils import embedding_functions

multilingual_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

def build_db():
    if os.path.exists("vectordb/chroma_store"):
        shutil.rmtree("vectordb/chroma_store")
        
    client = chromadb.PersistentClient(path="vectordb/chroma_store")
    
    collection = client.create_collection(
        name="scripture_verses",
        embedding_function=multilingual_ef
    )

    with open("data/bhagavad_gita.json", "r", encoding="utf-8") as f:
        gita_data = json.load(f)
    with open("data/thirukkural.json", "r", encoding="utf-8") as f:
        kural_data = json.load(f)

    documents = []
    metadatas = []
    ids = []

    for verse in gita_data:
        documents.append(verse["translation"]) 
        metadatas.append({"text_name": "Bhagavad Gita", "verse_id": verse["verse_id"]})
        ids.append(f"gita_{verse['verse_id']}")
        
    for verse in kural_data:
        documents.append(verse["translation"]) 
        metadatas.append({"text_name": "Thirukkural", "verse_id": verse["verse_id"]})
        ids.append(f"kural_{verse['verse_id']}")

    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print("✅ Multilingual Database Build Complete!")

if __name__ == "__main__":
    build_db()
