import re
from typing import List, Dict

CITATION_PATTERN = re.compile(r"\[([^\[\]]+?)\s+([\d.]+)\]")

def extract_citations(gemma_output: str) -> List[str]:
    citations = []
    for match in CITATION_PATTERN.finditer(gemma_output):
        text_name = match.group(1).strip()
        verse_id = match.group(2).strip()
        citations.append(f"{text_name} {verse_id}")
    return citations

def build_valid_reference_set(retrieved_chunks: List[Dict]) -> set:
    return {f"{c['text']} {c['verse_id']}" for c in retrieved_chunks}

def validate_citations(gemma_output: str, retrieved_chunks: List[Dict]) -> Dict:
    cited = extract_citations(gemma_output)
    valid_refs = build_valid_reference_set(retrieved_chunks)

    verified = [c for c in cited if c in valid_refs]
    unverified = [c for c in cited if c not in valid_refs]

    return {
        "verified": verified,
        "unverified": unverified,
        "all_valid": len(unverified) == 0,
        "total_citations": len(cited),
    }
