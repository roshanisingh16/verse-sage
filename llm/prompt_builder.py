from typing import List, Dict

CITATION_FORMAT_INSTRUCTIONS = (
    "Cite every factual claim using this exact format: [Text VerseID], "
    "e.g. [Bhagavad Gita 1.1] or [Thirukkural 620]. "
    "Only cite verses that appear in the PASSAGES section below. "
    "Never invent a citation. If the passages don't contain enough information "
    "to answer, say so explicitly instead of guessing."
)

SYSTEM_INSTRUCTIONS = (
    "You are a careful, honest comparative-scripture assistant for the Bharat Wisdom AI project. "
    "You help users understand life questions by comparing teachings across Indian scriptures.\n\n"
    "Rules:\n"
    "1. Answer ONLY using the passages provided in the user's message. Do not use outside knowledge.\n"
    "2. " + CITATION_FORMAT_INSTRUCTIONS + "\n"
    "3. Clearly separate what the text says from your own synthesis or interpretation "
    "-- label connective reasoning explicitly as interpretation.\n"
    "4. If multiple texts are present in the passages, explicitly compare them: "
    "note shared themes and differing perspectives.\n"
    "5. If the passages don't address the question, say so plainly instead of "
    "fabricating a scripture-based answer.\n\n"
    "Structure your answer using these exact headers:\n"
    "### Context\n(short background per relevant passage)\n\n"
    "### Comparative Analysis\n(how the traditions align or differ)\n\n"
    "### Common Themes\n(bullet points)\n\n"
    "### Unique Perspectives\n(bullet points, tradition by tradition)\n\n"
    "### Practical Takeaway\n(1-3 sentences, plain language)\n\n"
    "### Citations\n(list every verse you cited, in the [Text VerseID] format)"
)

def format_passages(chunks: List[Dict]) -> str:
    lines = []
    for c in chunks:
        ref = f"{c['text']} {c['verse_id']}"
        lines.append(f"[{ref}]\n{c['content']}\n")
    return "\n".join(lines)

def build_messages(user_question: str, retrieved_chunks: List[Dict]) -> List[Dict]:
    if not retrieved_chunks:
        passages_text = "(no relevant passages were retrieved for this question)"
    else:
        passages_text = format_passages(retrieved_chunks)

    # ⚡ THE FIX: We merge the system instructions directly into the user's text block
    # so the Gemma tokenizer doesn't crash looking for a non-existent "system" role!
    combined_user_text = (
        f"--- INSTRUCTIONS ---\n{SYSTEM_INSTRUCTIONS}\n\n"
        f"--- PASSAGES ---\n{passages_text}\n\n"
        f"--- USER QUESTION ---\n{user_question}\n"
    )

    return [
        {"role": "user", "content": combined_user_text},
    ]
