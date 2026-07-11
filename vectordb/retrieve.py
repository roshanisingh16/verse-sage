import chromadb
from chromadb.utils import embedding_functions

multilingual_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

def get_collection():
    client = chromadb.PersistentClient(path="vectordb/chroma_store")
    return client.get_collection(
        name="scripture_verses",
        embedding_function=multilingual_ef
    )

def query_verses(question, n_results=2):
    collection = get_collection()
    
    gita_results = collection.query(
        query_texts=[question], 
        n_results=n_results,
        where={"text_name": "Bhagavad Gita"}
    )
    
    kural_results = collection.query(
        query_texts=[question], 
        n_results=n_results,
        where={"text_name": "Thirukkural"}
    )
    
    output = []
    
    if gita_results['documents'] and gita_results['documents'][0]:
        for doc, meta in zip(gita_results['documents'][0], gita_results['metadatas'][0]):
            output.append({"text": meta['text_name'], "verse_id": meta['verse_id'], "content": doc})
            
    if kural_results['documents'] and kural_results['documents'][0]:
        for doc, meta in zip(kural_results['documents'][0], kural_results['metadatas'][0]):
            output.append({"text": meta['text_name'], "verse_id": meta['verse_id'], "content": doc})
            
    return output
