import gradio as gr


def answer_question(user_input):
    return f"You asked: {user_input}"


def clear_fields():
    return "", "", "Sources will appear here."


examples = [
    ["What is karma?"],
    ["Compare compassion in Bhagavad Gita and Dhammapada."],
    ["What do Indian scriptures say about anger?"],
    ["How should a leader behave?"],
    ["What is the meaning of selfless action?"],
    ["How do Ramayana and Guru Granth Sahib define service?"],
]

css = """
.gradio-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
}

#hero {
    text-align: center;
    padding: 2rem 0 2rem;
    max-width: 980px;
    margin: 0 auto;
}

#hero h1 {
    font-size: clamp(2.3rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 0.45rem 0;
    color: #111827;
}

#hero .subtitle {
    font-size: clamp(1.05rem, 2vw, 1.35rem);
    font-weight: 600;
    color: #374151;
    margin-bottom: 0.75rem;
}

#hero .description {
    font-size: 1rem;
    line-height: 1.75;
    color: #4b5563;
    max-width: 920px;
    margin: 0 auto;
}

.card {
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 20px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
    padding: 1.2rem 1.2rem 1rem;
}

.section-title {
    margin: 0.1rem 0 0.5rem 0;
}

.footer {
    text-align: center;
    color: #6b7280;
    padding: 1rem 0 0.25rem;
    font-size: 0.95rem;
    line-height: 1.6;
}

.small-muted {
    color: #6b7280;
}

#question_box textarea {
    min-height: 140px !important;
}
"""

theme = gr.themes.Soft(
    primary_hue="slate",
    secondary_hue="slate",
    neutral_hue="gray",
)

with gr.Blocks(theme=theme, css=css, title="VerseSage") as demo:
    gr.Markdown(
       """
    <div id="hero">
       <h1>VerseSage</h1>

       <div class="subtitle">
            AI-powered Cross-Scripture Wisdom Engine
       </div>

       <div class="description">
            Compare teachings from Indian scriptures using Google Gemma-4-E4B and Retrieval-Augmented Generation.
            Ask questions about life, ethics, duty, compassion, leadership, relationships, spirituality, and wisdom.
       </div>

       <br>

       <div class="small-muted">
         Responses are generated using Google Gemma-4-E4B with RAG Pipeline.
         Please refer to the original scriptures for deeper study.
         </div>
      </div>
      """
    )

    with gr.Row(equal_height=True):
        with gr.Column(scale=7, min_width=680):
            with gr.Column(elem_classes="card"):
                gr.Markdown("## Ask your question")
                question_box = gr.Textbox(
                    label="Ask your question",
                    placeholder="Ask anything about karma, leadership, compassion, duty, relationships, or spirituality.",
                    lines=4,
                    max_lines=8,
                    show_label=True,
                    elem_id="question_box",
                )

                with gr.Row():
                    get_wisdom_btn = gr.Button("Get Wisdom", variant="primary", scale=2,)
                    clear_btn = gr.Button("Clear", scale=1,)

                status = gr.Markdown("**Status:** Ready")
                gr.Markdown("## AI Response")
                response_box = gr.Textbox(
                    label="AI Response",
                    placeholder="Model response will appear here.",
                    lines=8,
                    interactive=False,
                    show_label=True,
                )

                gr.Markdown("## Sources")
                sources_box = gr.Textbox(
                    label="Sources",
                    value="Sources will appear here.",
                    lines=3,
                    interactive=False,
                    show_label=True,
                )

                gr.Markdown("## Example Questions")
                gr.Examples(
                    examples=examples,
                    inputs=question_box,
                    label=None,
                    cache_examples=False,
                )
                gr.Markdown(
                    """
                  ---
                    
                  ## About VerseSage
                  
                  VerseSage is an AI-powered Cross-Scripture
                  Wisdom Engine that enables users to
                  explor, compare, and understand teachings
                  from major Indian Scriptures.
                  
                  Built using Google Gemma-4-E4B and
                  Retrieval-Augmented Generation (RAG),
                  VerseSage grounds responses in authentic
                  scriptural knowledge while providing meaningful, comparative insights.
                  """
                )
                gr.Markdown(
                    """
                    <div class="footer">
                        Built for <b> Gemma for Bharat Hackathon 2026 <b><br>
                        Powered by Google Gemma-4-E4B | ChromaDB | Sentence Transformers | Gradio.
                    </div>
                    """
                )

        with gr.Column(scale=3, min_width=280):
            with gr.Column(elem_classes=["card"]):
                gr.Markdown("## Supported Scriptures")
                gr.Markdown(
                    """
                    ✓ Bhagavad Gita  
                    ✓ Upanishads  
                    ✓ Thirukkural  
                    ✓ Dhammapada  
                    ✓ Guru Granth Sahib  
                    ✓ Ramayana
                    """
                )

                gr.Markdown("## Technology Stack")
                gr.Markdown(
                    """
                    • Google Gemma-4-E4B  
                    • Retrieval-Augmented Generation 
                    • ChromaDB  
                    • Sentence Transformers  
                    • Gradio
                    """
                )

    get_wisdom_btn.click(
        fn=answer_question,
        inputs=question_box,
        outputs=response_box,
    )

    question_box.submit(
        fn=answer_question,
        inputs=question_box,
        outputs=response_box,
    )

    clear_btn.click(
        fn=clear_fields,
        inputs=[],
        outputs=[question_box, response_box, sources_box],
    )


if __name__ == "__main__":
    demo.launch()