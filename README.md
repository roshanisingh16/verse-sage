# VerseSage

### AI-powered Cross-Scripture Wisdom Engine

*Bridging India's timeless spiritual wisdom with modern Artificial Intelligence using Google Gemma-3-E4B-it.*

[![Google Gemma-3-E4B-it](https://img.shields.io/badge/Google-Gemma--3--E4B-it-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-UI-F97316?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-00A67E?style=for-the-badge&logo=databricks&logoColor=white)](https://www.trychroma.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Hugging Face Spaces](https://img.shields.io/badge/🤗_Hugging_Face-Spaces-FFD21E?style=for-the-badge)](https://huggingface.co/spaces)
[![Open Source](https://img.shields.io/badge/Open_Source-❤️-red?style=for-the-badge)](https://github.com/roshanisingh16/verse-sage)
[![RAG Pipeline](https://img.shields.io/badge/RAG-Pipeline-blueviolet?style=for-the-badge)](https://github.com/roshanisingh16/verse-sage)



**VerseSage** uses semantic search and Retrieval-Augmented Generation (RAG) to let anyone ask natural-language questions across Indian scriptures — and receive citation-backed, comparative answers powered by **Google Gemma-3-E4B-it**. The current release supports the **Bhagavad Gita** and **Thirukkural**, with more scriptures coming soon.


[Overview](#-overview) · [Features](#-features) · [Scriptures](#-supported-scriptures) · [Architecture](#-system-architecture) · [Installation](#-installation) · [Usage](#-usage) · [Roadmap](#-future-roadmap) · [Contributing](#-contributing)

---

## Overview

India's spiritual and philosophical heritage spans thousands of years and encompasses millions of verses across dozens of sacred texts — from the Bhagavad Gita to the Thirukkural. These scriptures hold profound wisdom on ethics, consciousness, duty, compassion, and the nature of existence.

Yet accessing this wisdom remains surprisingly difficult:

- **Traditional search is keyword-based.** Searching for "forgiveness" will miss verses that discuss *kshama*, *daya*, or *karuna* — words that carry the same meaning in different scriptural contexts.
- **Scriptures live in silos.** A student of the Bhagavad Gita rarely encounters the Thirukkural's parallel teachings on the same topic, and vice versa.
- **AI can hallucinate.** General-purpose language models may fabricate verses, misattribute quotes, or invent scripture references that do not exist.

**VerseSage** currently enables comparative reasoning between the **Bhagavad Gita** and the **Thirukkural**, with a modular architecture designed to support additional scriptures in future releases. It solves these problems by combining:

1. **Semantic search** — understanding the *meaning* behind a question, not just its keywords.
2. **Cross-scripture retrieval** — pulling relevant verses from multiple traditions simultaneously.
3. **Retrieval-Augmented Generation (RAG)** — grounding every AI response in real, retrieved passages so that nothing is fabricated.
4. **Comparative reasoning** — using Google Gemma-3-E4B-it to synthesize insights across the Bhagavad Gita and Thirukkural, highlighting convergences and divergences.
5. **Citation-backed answers** — every claim in the response is traceable to a specific verse, chapter, and scripture.

The result is an AI system that is **accurate**, **transparent**, **cross-traditional**, and **trustworthy** — one that treats India's spiritual texts with the scholarly rigor they deserve.

---

## Problem Statement

| # | Problem | Impact |
|---|---------|--------|
| 1 | Existing scripture tools search **only one text** at a time | Users miss related teachings from other traditions |
| 2 | Keyword-based search **misses semantic meaning** | Conceptually relevant verses are never surfaced |
| 3 | **Cross-scripture comparison** requires expert-level knowledge | Interfaith and comparative study remains inaccessible |
| 4 | General-purpose LLMs **hallucinate** scripture references | Users cannot trust AI-generated spiritual guidance |
| 5 | No single platform offers **grounded, citation-backed** answers across Indian scriptures | Scholarly rigor is sacrificed for convenience |

> **In short:** There is no existing system that combines semantic understanding, multi-scripture retrieval, comparative reasoning, and citation verification — all in one accessible interface.

---

## Solution

VerseSage implements a complete **Retrieval-Augmented Generation (RAG)** pipeline that transforms a user's natural-language question into a grounded, citation-backed, cross-scripture response:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        VerseSage RAG Pipeline                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   User Query ──► Embedding ──► Vector Search ──► Top-K Retrieval   │
│                                                                     │
│   Retrieved Verses ──► Prompt Construction ──► Gemma-3-E4B-it LLM     │
│                                                                     │
│   LLM Output ──► Comparative Reasoning ──► Citation Validation     │
│                                                                     │
│   Validated Response ──► Gradio UI ──► User                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

1. The user asks a question in plain language (e.g., *"What do Indian scriptures say about controlling anger?"*).
2. The question is embedded into a dense vector using **Sentence Transformers**.
3. **ChromaDB** performs a nearest-neighbor search across the entire multi-scripture knowledge base.
4. The top-K most relevant verses — along with their metadata (scripture, chapter, verse number, language) — are retrieved.
5. A structured prompt is constructed that includes the original question and the retrieved passages.
6. **Google Gemma-3-E4B-it** reasons over the passages, compares teachings across traditions, and generates a coherent, comparative response.
7. Every claim in the response is backed by a specific citation from the retrieved verses.

> The user never sees a hallucinated verse. Every answer is grounded in authentic text.

---

##  Features

| Feature | Description |
|---------|-------------|
|  **Semantic Scripture Search** | Understands the *meaning* of your question, not just keywords — surfaces conceptually relevant verses across traditions |
|  **Cross-Scripture Comparison** | Retrieves and compares teachings from the Bhagavad Gita and Thirukkural in a single response, with more scriptures planned for future releases |
|  **Google Gemma-3-E4B-it Reasoning** | Leverages Google's state-of-the-art language model for nuanced philosophical reasoning and synthesis |
|  **Retrieval-Augmented Generation** | Grounds every response in real, retrieved scripture passages — eliminates hallucination |
|  **Citation-Backed Answers** | Every claim is traceable to a specific verse, chapter, and scripture — fully auditable |
|  **ChromaDB Vector Search** | High-performance vector similarity search for sub-second retrieval across thousands of verses |
|  **Metadata-Aware Retrieval** | Filters and ranks results using scripture name, chapter, verse number, language, and thematic tags |
|  **Gradio Interface** | Clean, intuitive web UI accessible from any browser — no installation required for end users |
|  **Modular Architecture** | Cleanly separated components (data, embeddings, vector DB, LLM, pipeline) for easy extension and maintenance |
|  **Fast Retrieval** | Optimized vector indexing delivers relevant verses in milliseconds |
|  **Future Multilingual Support** | Architecture designed to support Hindi, Tamil, Punjabi, Pali, and other Indian languages |

---

## Supported Scriptures

The current release of VerseSage supports the following scriptures:

| Scripture | Language | Description | Significance |
|-----------|----------|-------------|--------------|
| **Bhagavad Gita** | Sanskrit | 700 verses of Lord Krishna's counsel to Arjuna on duty, righteousness, and the nature of the self | Central philosophical text of Hinduism; foundational to Indian ethics and metaphysics |
| **Thirukkural** | Tamil | 1,330 couplets by Thiruvalluvar on virtue, wealth, and love — a secular ethical masterpiece | A cornerstone of Tamil literature; often called the "universal scripture" for its non-sectarian wisdom |

> **Why these two?** The Bhagavad Gita and the Thirukkural represent two of India's most influential philosophical traditions — spanning Sanskrit and Tamil, Hindu philosophy and secular ethics — providing a strong foundation for cross-scripture comparative reasoning. The modular architecture is designed to incorporate additional scriptures (Upanishads, Ramayana, Guru Granth Sahib, Dhammapada, and more) in future releases.

---

##  Tech Stack

| Layer | Technology | Role |
|-------|-----------|------|
| **Frontend** | [Gradio](https://gradio.app) | Interactive web interface for query input and response display |
| **Language** | [Python 3.10+](https://python.org) | Core application logic, pipeline orchestration, and data processing |
| **LLM** | [Google Gemma-3-E4B-it](https://ai.google.dev/gemma) | Comparative reasoning, response generation, and philosophical synthesis |
| **Embeddings** | [Sentence Transformers](https://www.sbert.net) | Dense vector encoding of queries and scripture passages for semantic search |
| **Vector Database** | [ChromaDB](https://www.trychroma.com) | Persistent vector storage, indexing, and approximate nearest-neighbor retrieval |
| **Deployment** | [Hugging Face Spaces](https://huggingface.co/spaces) | Cloud hosting and public access for the live demo |
| **Version Control** | [Git & GitHub](https://github.com/roshanisingh16/verse-sage) | Source code management, collaboration, and issue tracking |

---

## System Architecture

```
                            ┌──────────────────────┐
                            │     User Question     │
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │   Gradio Interface    │
                            │  (Web UI / API)       │
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │  Sentence Transformer │
                            │  Query Embedding      │
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │   ChromaDB Vector     │
                            │   Similarity Search   │
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │  Retrieve Top-K       │
                            │  Verses + Metadata    │
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │  Prompt Construction  │
                            │  (Query + Verses)     │
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │  Google Gemma-3-E4B-it   │
                            │  Comparative Reasoning│
                            └──────────┬───────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │  Citation-Backed      │
                            │  Response to User     │
                            └──────────────────────┘
```

### Pipeline Stages Explained

| Stage | Component | What Happens |
|-------|-----------|--------------|
| **1. Input** | Gradio Interface | The user types a natural-language question into the web UI |
| **2. Embedding** | Sentence Transformers | The question is converted into a dense vector that captures its semantic meaning |
| **3. Retrieval** | ChromaDB | The query vector is compared against all indexed scripture vectors; the top-K most similar passages are returned |
| **4. Enrichment** | Metadata Engine | Each retrieved passage is annotated with its scripture name, chapter, verse number, and language |
| **5. Prompt Assembly** | Pipeline Module | The original question and the retrieved, annotated passages are composed into a structured prompt |
| **6. Reasoning** | Google Gemma-3-E4B-it | The LLM reads the prompt, performs comparative analysis across scriptures, and generates a synthesized response |
| **7. Output** | Gradio Interface | The citation-backed response — with verse references — is displayed to the user |

---

##  How It Works

### Step 1 — User Question
The user asks a question in natural language. No special syntax is required.

> *Example: "What do Indian scriptures say about the importance of truth?"*

### Step 2 — Query Embedding
The question is passed through a **Sentence Transformer** model, producing a high-dimensional dense vector that encodes the semantic meaning of the query — not just its surface-level keywords.

### Step 3 — Vector Retrieval
The query embedding is sent to **ChromaDB**, which performs an approximate nearest-neighbor search across the pre-indexed scripture knowledge base. The top-K most semantically similar verses are retrieved along with their metadata.

### Step 4 — Prompt Construction
A structured prompt is assembled containing:
- The original user question
- The retrieved scripture passages (with full metadata)
- Instructions for comparative analysis and citation formatting

### Step 5 — Gemma-3-E4B-it Reasoning
**Google Gemma-3-E4B-it** receives the prompt and performs:
- **Comprehension** — understanding each retrieved passage in context
- **Comparison** — identifying convergences and divergences across scriptures
- **Synthesis** — generating a coherent, multi-perspective response

### Step 6 — Citation Validation
Every claim in the generated response is linked to a specific retrieved verse. The system ensures that no unsupported statements are included — if the retrieved passages do not support a claim, it is not made.

### Step 7 — Final Response
The user receives a well-structured answer that:
- Addresses their question directly
- Draws from multiple scriptures
- Cites specific verses and chapters
- Highlights cross-scripture insights

---

## 🗄 Knowledge Base

### Metadata Schema

The current vector database contains embeddings for the **Bhagavad Gita** and the **Thirukkural**. Every verse in the VerseSage knowledge base is stored with rich metadata to enable precise, filterable retrieval:

```json
{
  "id": "bg_2_47",
  "text": "You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions.",
  "metadata": {
    "scripture": "Bhagavad Gita",
    "chapter": 2,
    "verse": 47,
    "language": "Sanskrit",
    "theme": ["duty", "detachment", "karma yoga"],
    "speaker": "Lord Krishna",
    "translation_source": "Swami Mukundananda"
  }
}
```

### Why Metadata Matters

| Metadata Field | Retrieval Benefit |
|---------------|-------------------|
| `scripture` | Enables filtering by specific scripture or cross-scripture comparison |
| `chapter` / `verse` | Provides exact citation for verification and scholarly reference |
| `language` | Supports future multilingual retrieval and language-aware ranking |
| `theme` | Enables thematic clustering and tag-based filtering |
| `speaker` | Allows attribution-aware retrieval (e.g., "What did Lord Krishna say about…") |
| `translation_source` | Ensures transparency and academic integrity of translations used |

> **Metadata transforms raw text retrieval into structured, scholarly-grade knowledge retrieval.**

---

## Why RAG?

Large Language Models are powerful, but they have a fundamental limitation: **they can hallucinate**. When asked about scripture, a general-purpose LLM might fabricate verses, misattribute quotes, or invent references that do not exist. For a system dealing with sacred texts, this is unacceptable.

**Retrieval-Augmented Generation (RAG)** solves this by ensuring the LLM only reasons over passages that were actually retrieved from the knowledge base.

### Without RAG vs. With RAG

```
┌─────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│           WITHOUT RAG               │    │              WITH RAG                    │
├─────────────────────────────────────┤    ├──────────────────────────────────────────┤
│                                     │    │                                          │
│  User Question                      │    │  User Question                           │
│       │                             │    │       │                                  │
│       ▼                             │    │       ▼                                  │
│  LLM (trained knowledge only)       │    │  Embedding ──► Vector DB ──► Retrieved   │
│       │                             │    │  Verses                                  │
│       ▼                             │    │       │                                  │
│  ⚠️  Response may contain:          │    │       ▼                                  │
│  • Fabricated verses                │    │  LLM + Retrieved Verses                  │
│  • Wrong attributions               │    │       │                                  │
│  • Invented references              │    │       ▼                                  │
│  • No citations                     │    │  ✅ Response contains:                   │
│  • No way to verify                 │    │  • Real verses only                      │
│                                     │    │  • Correct attributions                  │
│  ❌ Untrustworthy                   │    │  • Verifiable references                 │
│                                     │    │  • Full citations                        │
│                                     │    │  • Auditable and transparent             │
│                                     │    │                                          │
│                                     │    │  ✅ Trustworthy                          │
└─────────────────────────────────────┘    └──────────────────────────────────────────┘
```

| Dimension | Without RAG | With RAG (VerseSage) |
|-----------|-------------|----------------------|
| **Hallucination** | High risk — LLM may invent verses | Eliminated — only retrieved verses are used |
| **Grounding** | None — responses float in parametric memory | Full — every response is anchored to real passages |
| **Citations** | Absent or fabricated | Authentic — traceable to specific verse, chapter, and scripture |
| **Transparency** | Black box | Auditable — users can verify every claim |
| **Trustworthiness** | Low — no verification possible | High — scholarly-grade accuracy and accountability |

---

##  Project Structure

```
verse-sage/
├── app.py                  # Application entry point — launches the Gradio interface
├── data/                   # Scripture datasets (JSON/CSV) with verse text and metadata
├── embeddings/             # Sentence Transformer embedding logic and model configuration
├── vectordb/               # ChromaDB initialization, indexing, and query interface
├── llm/                    # Google Gemma-3-E4B-it integration, prompt templates, and inference
├── pipeline/               # End-to-end RAG pipeline orchestration (retrieval → generation)
├── docs/                   # Project documentation, design decisions, and API reference
├── assets/                 # Images, banners, diagrams, and visual assets
├── requirements.txt        # Python dependency manifest
└── README.md               # This file
```

| Directory / File | Purpose |
|-----------------|---------|
| `app.py` | Main entry point — initializes components and launches the Gradio web server |
| `data/` | Stores pre-processed scripture data with verse text, translations, and structured metadata |
| `embeddings/` | Handles loading the Sentence Transformer model and encoding text into dense vectors |
| `vectordb/` | Manages the ChromaDB collection — indexing scripture vectors, persisting the database, and running similarity queries |
| `llm/` | Contains the Google Gemma-3-E4B-it integration — model loading, prompt template construction, and inference logic |
| `pipeline/` | Orchestrates the full RAG pipeline — from receiving a query to returning a citation-backed response |
| `docs/` | Supplementary documentation including architecture diagrams, design rationale, and API docs |
| `assets/` | Static assets — banner images, architecture diagrams, and screenshots for the README |
| `requirements.txt` | Lists all Python dependencies with pinned versions for reproducible environments |

---

## ⚙ Installation

### Prerequisites

- Python 3.10 or higher
- Git
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/roshanisingh16/verse-sage.git
cd verse-sage
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Linux / macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The Gradio interface will launch at `http://localhost:7860`. Open this URL in your browser to start asking questions.

---

##  Usage

1. **Open the application** — Navigate to `http://localhost:7860` in your browser (or visit the Hugging Face Spaces deployment).
2. **Type your question** — Ask any question about the Bhagavad Gita, the Thirukkural, or comparative topics in natural language. No special syntax or keywords required.
3. **Submit** — Click the submit button or press Enter.
4. **Read the response** — VerseSage will return a comparative answer drawing from the Bhagavad Gita and the Thirukkural, with each claim backed by specific verse citations.
5. **Explore further** — Ask follow-up questions, compare specific teachings, or dive deeper into a particular topic.

> **Tip:** The more specific your question, the more focused and insightful the response. Instead of *"Tell me about karma"*, try *"How do the Bhagavad Gita and the Thirukkural differ in their understanding of karma and duty?"*

---

##  Example Questions

Here are meaningful questions you can ask VerseSage to explore cross-scripture wisdom from the Bhagavad Gita and the Thirukkural:

| # | Question |
|---|----------|
| 1 | What do the Bhagavad Gita and the Thirukkural say about controlling anger and cultivating patience? |
| 2 | How do the Bhagavad Gita and the Thirukkural differ in their teachings on detachment and renunciation? |
| 3 | What is the concept of dharma in the Bhagavad Gita, and how does it compare to virtue in the Thirukkural? |
| 4 | How does the Thirukkural define a virtuous life, and are there parallels in the Bhagavad Gita? |
| 5 | What teachings on compassion and kindness are shared between the Bhagavad Gita and the Thirukkural? |
| 6 | What do the Bhagavad Gita and the Thirukkural say about the importance of truthfulness and integrity? |
| 7 | How is the concept of karma and duty explained in the Bhagavad Gita compared to the Thirukkural? |
| 8 | What guidance do the Bhagavad Gita and the Thirukkural offer on self-discipline and inner peace? |
| 9 | How do the Bhagavad Gita and the Thirukkural address the relationship between wealth, ethics, and spiritual growth? |
| 10 | What do the Bhagavad Gita and the Thirukkural teach about leadership and righteous conduct? |
| 11 | How do the Bhagavad Gita and the Thirukkural describe the qualities of an ideal person? |
| 12 | What perspectives on love, friendship, and human relationships appear in the Bhagavad Gita and the Thirukkural? |

---

##  Novelty

VerseSage is not just another scripture search tool. It introduces several innovations that set it apart:

###  Cross-Scripture Comparative Reasoning
No existing system performs **automated comparative analysis** across Indian scriptures in a single query. VerseSage currently retrieves relevant verses from the Bhagavad Gita and the Thirukkural — and uses Google Gemma-3-E4B-it to synthesize insights across these two foundational traditions, with a modular architecture ready to incorporate additional scriptures.

###  Citation-Backed AI
Every claim in VerseSage's response is traceable to a specific verse, chapter, and scripture. Unlike general-purpose chatbots, **nothing is fabricated** — the RAG pipeline ensures that the LLM only reasons over real, retrieved passages.

### Metadata-Driven Retrieval
Rich metadata (scripture, chapter, verse, language, theme, speaker) enables **structured, filterable retrieval** that goes far beyond naive text similarity.

###  Explainable AI
Users can see *which* verses informed the response and *from which* scriptures they were drawn — making the system transparent and auditable.

### Semantic Understanding
Sentence Transformer embeddings capture the deep semantic meaning of both queries and scripture passages, enabling retrieval that **transcends language and keyword barriers**.

### Cultural Knowledge Preservation
VerseSage digitizes, indexes, and makes searchable India's vast spiritual heritage — contributing to the **preservation and accessibility** of knowledge that has guided civilizations for millennia.

---

## Applications

| Domain | Application |
|--------|-------------|
| **Education** | Interactive teaching aid for courses on Indian philosophy, comparative religion, and ethics |
| **Research** | Accelerates scholarly research by enabling instant cross-scripture semantic search and comparison |
| **Comparative Religion** | Facilitates interfaith dialogue by surfacing shared values and distinct perspectives across traditions |
| **Spiritual Learning** | Provides accessible, citation-backed guidance for personal spiritual exploration and study |
| **Knowledge Discovery** | Reveals unexpected connections and thematic patterns across scriptures that manual study might miss |
| **Cultural Preservation** | Digitizes and indexes India's spiritual heritage, ensuring it remains accessible for future generations |

---

## 📈 Future Roadmap

|  Feature | Description |
|---------|-------------|
|  **Expand Scripture Knowledge Base** | Integrate additional Indian scriptures including the **Upanishads**, **Ramayana**, **Guru Granth Sahib**, **Dhammapada**, and other classical Indian texts. The modular architecture is already designed to support easy expansion |
|  **Voice Interaction** | Ask questions and receive answers via speech — enabling hands-free, accessible scripture exploration |
|  **Regional Language Support** | Hindi, Tamil, Punjabi, Pali, and other Indian language interfaces and retrieval |
|  **Even More Scriptures** | Further expand to include the Vedas, Mahabharata, Yoga Sutras, Jain Agamas, and more |
|  **Mobile App** | Native Android and iOS applications for on-the-go scripture exploration |
|  **Personalized Recommendations** | AI-driven suggestions based on user interests, reading history, and spiritual goals |
|  **Conversation History** | Persistent chat sessions with the ability to revisit and continue past explorations |
|  **Scholar Commentaries** | Integration of traditional commentaries (Shankaracharya, Ramanujacharya, etc.) alongside verse retrieval |
|  **Citation Visualization** | Interactive visual maps showing which scriptures and verses informed each part of the response |

---

## Contributing

Contributions are welcome and appreciated! Whether you're fixing a bug, adding a scripture, improving documentation, or proposing a new feature — every contribution makes VerseSage better.

### How to Contribute

1. **Fork** the repository

   ```bash
   git clone https://github.com/your-username/verse-sage.git
   ```

2. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** — follow existing code style and conventions

4. **Commit** with a clear, descriptive message

   ```bash
   git commit -m "feat: add Yoga Sutras to knowledge base"
   ```

5. **Push** to your fork

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** — describe your changes, link any related issues, and request a review

### Contribution Guidelines

- Write clear, well-documented code
- Add tests for new functionality where applicable
- Keep PRs focused — one feature or fix per PR
- Be respectful and constructive in all discussions

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 VerseSage Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Acknowledgements

VerseSage stands on the shoulders of remarkable open-source projects and communities:

- **[Google Gemma](https://ai.google.dev/gemma)** — for Gemma-3-E4B-it, the powerful and efficient language model at the heart of VerseSage's reasoning engine
- **[Hugging Face](https://huggingface.co)** — for the Transformers ecosystem, model hosting, and Spaces deployment platform
- **[ChromaDB](https://www.trychroma.com)** — for the fast, developer-friendly vector database that powers our semantic search
- **[Sentence Transformers](https://www.sbert.net)** — for state-of-the-art sentence embedding models that make semantic retrieval possible
- **[Gradio](https://gradio.app)** — for the elegant, rapid-prototyping UI framework
- **The Open-Source Community** — for the countless libraries, tools, and ideas that make projects like this possible
- **Google Developers Group** — for fostering developer communities and supporting AI innovation in India
- **Gemma for Bharat Hackathon** — for creating the platform and inspiration to build AI solutions rooted in India's cultural heritage

---
## Why VerseSage?

*India's spiritual texts have guided billions of people across millennia — offering profound insights on consciousness, ethics, duty, compassion, and the nature of existence. Yet this wisdom has remained locked in individual texts, accessible only to those with the linguistic expertise and scholarly patience to navigate thousands of verses across multiple traditions.*

*VerseSage changes this.*

*By combining the semantic power of modern AI embeddings, the precision of Retrieval-Augmented Generation, and the reasoning capabilities of Google Gemma-3-E4B-it, VerseSage makes it possible for anyone — a student, a researcher, a seeker — to ask a question in plain language and receive a thoughtful, comparative, citation-backed answer. The current release draws from the Bhagavad Gita and the Thirukkural, with a modular architecture ready to embrace more of India's scriptural heritage.*

*This is not about replacing human wisdom with artificial intelligence. It is about using AI as a bridge — connecting seekers to the timeless teachings that have always been there, waiting to be discovered.*

**VerseSage: Where ancient wisdom meets modern intelligence.** 🙏

---

Built with ❤️ for the Google Gemma for Bharat Hackathon


[![Star this repo](https://img.shields.io/github/stars/roshanisingh16/verse-sage?style=social)](https://github.com/roshanisingh16/verse-sage)
[![Fork this repo](https://img.shields.io/github/forks/roshanisingh16/verse-sage?style=social)](https://github.com/roshanisingh16/verse-sage/fork)

