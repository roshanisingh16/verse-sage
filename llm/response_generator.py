from llm.prompt_builder import build_messages
from llm.citation_validator import validate_citations
from llm.gemma_client import GemmaClient

_client = None

def get_client() -> GemmaClient:
    global _client
    if _client is None:
        _client = GemmaClient()
    return _client

def generate_answer(user_question: str, retrieved_chunks: list) -> dict:
    messages = build_messages(user_question, retrieved_chunks)
    raw_output = get_client().generate(messages)
    validation = validate_citations(raw_output, retrieved_chunks)

    return {
        "answer_text": raw_output,
        "citations_verified": validation["verified"],
        "citations_unverified": validation["unverified"],
        "all_citations_valid": validation["all_valid"],
        "retrieved_scriptures": sorted({c["text"] for c in retrieved_chunks}),
    }
