import json
import urllib.request
import os
from sentence_transformers import SentenceTransformer
import chromadb

os.makedirs('data', exist_ok=True)
os.makedirs('vectordb', exist_ok=True)


def fetch_gita():
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/gita/gita/main/data/verse.json",
        "verse.json"
    )
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/gita/gita/main/data/translation.json",
        "translation.json"
    )
    with open('verse.json', encoding='utf-8') as f:
        verses = json.load(f)
    with open('translation.json', encoding='utf-8') as f:
        translations = json.load(f)

    trans_lookup = {}
    for t in translations:
        if t['lang'] == 'english' and t['authorName'] == 'Swami Adidevananda':
            trans_lookup[t['verse_id']] = t['description']

    final = []
    for v in verses:
        entry = {
            'text_name': 'Bhagavad Gita',
            'verse_id': f"{v['chapter_number']}.{v['verse_number']}",
            'chapter': v['chapter_number'],
            'verse_number': v['verse_number'],
            'original_text': v['text'].strip(),
            'translation': trans_lookup.get(v['id'], '').strip(),
            'theme_tags': []
        }
        final.append(entry)

    with open('data/bhagavad_gita.json', 'w', encoding='utf-8') as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print(f"Gita: {len(final)} verses saved.")
    return final


def fetch_thirukkural():
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/tk120404/thirukkural/master/thirukkural.json",
        "thirukkural_raw.json"
    )
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/tk120404/thirukkural/master/detail.json",
        "detail.json"
    )
    with open('thirukkural_raw.json', encoding='utf-8') as f:
        kurals = json.load(f)['kural']
    with open('detail.json', encoding='utf-8') as f:
        detail = json.load(f)[0]

    kural_to_chapter = {}
    chapter_counter = 0
    for section in detail['section']['detail']:
        section_name = section['translation']
        for group in section['chapterGroup']['detail']:
            for chapter in group['chapters']['detail']:
                chapter_counter += 1
                for n in range(chapter['start'], chapter['end'] + 1):
                    kural_to_chapter[n] = {
                        'chapter_number': chapter_counter,
                        'chapter_name': chapter['translation'],
                        'section_name': section_name
                    }

    final = []
    for k in kurals:
        num = k['Number']
        ch = kural_to_chapter.get(num, {})
        entry = {
            'text_name': 'Thirukkural',
            'verse_id': f"{ch.get('chapter_number')}.{num}",
            'chapter': ch.get('chapter_number'),
            'chapter_name': ch.get('chapter_name'),
            'section': ch.get('section_name'),
            'verse_number': num,
            'original_text': (k['Line1'] + ' ' + k['Line2']).strip(),
            'translation': k['explanation'].strip(),
            'theme_tags': []
        }
        final.append(entry)

    with open('data/thirukkural.json', 'w', encoding='utf-8') as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print(f"Thirukkural: {len(final)} kurals saved.")
    return final


def build_embeddings(gita, thirukkural):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path="vectordb/chroma_store")
    collection = client.get_or_create_collection(name="scripture_verses")

    def add_to_collection(verses):
        for v in verses:
            embedding = model.encode(v['translation']).tolist()
            collection.add(
                ids=[f"{v['text_name']}_{v['verse_id']}"],
                embeddings=[embedding],
                documents=[v['translation']],
                metadatas=[{
                    "text_name": v['text_name'],
                    "verse_id": v['verse_id'],
                    "chapter": v.get('chapter', 0)
                }]
            )

    add_to_collection(gita)
    add_to_collection(thirukkural)
    print(f"Total verses in collection: {collection.count()}")


if __name__ == "__main__":
    gita = fetch_gita()
    thirukkural = fetch_thirukkural()
    build_embeddings(gita, thirukkural)