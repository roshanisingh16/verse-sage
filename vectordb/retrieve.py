import chromadb

def get_collection():
    client = chromadb.PersistentClient(path="vectordb/chroma_store")
    return client.get_collection(name="scripture_verses")

def query_verses(question, n_results=5):
    collection = get_collection()
    results = collection.query(query_texts=[question], n_results=n_results)
    output = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        output.append({
            "text": meta['text_name'],
            "verse_id": meta['verse_id'],
            "content": doc
        })
    return output

if __name__ == "__main__":
    results = query_verses("What is the nature of duty?")
    for r in results:
        print(f"[{r['text']} {r['verse_id']}] {r['content']}")