import streamlit as st
from vectordb.retrieve import query_verses
from llm.response_generator import generate_answer

# 1. Page Configuration
st.set_page_config(
    page_title="Verse Sage | Multilingual Scripture AI",
    page_icon="🪷",
    layout="centered"
)

# 2. Header UI
st.title("🪷 Verse Sage")
st.markdown("**Multilingual Scripture AI:** Ask a life question and receive comparative wisdom from the Bhagavad Gita and Thirukkural.")
st.divider()

# 3. Chat History State Management
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. User Input & Processing
if prompt := st.chat_input("e.g., How should I deal with failure?"):
    
    # Add user message to chat state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("Consulting the scriptures... ⚡"):
            try:
                # Retrieve matching verses from ChromaDB
                retrieved_chunks = query_verses(prompt, n_results=2)
                
                if not retrieved_chunks:
                    st.warning("Could not find relevant scriptures for this specific query.")
                else:
                    # Generate the comparative answer using Gemma 2 2B
                    result = generate_answer(prompt, retrieved_chunks)
                    
                    # Display the main answer
                    st.markdown(result["answer_text"])
                    
                    # Create an expandable UI section for the Citation Checker
                    with st.expander("🔍 Citation Validation", expanded=False):
                        verified = ", ".join(set(result["citations_verified"])) if result["citations_verified"] else "None"
                        unverified = ", ".join(set(result["citations_unverified"])) if result["citations_unverified"] else "None"
                        
                        st.success(f"**Verified Citations:** {verified}")
                        if unverified != "None":
                            st.error(f"**Unverified/Hallucinated Citations:** {unverified}")
                        else:
                            st.info("**Unverified Citations:** None")

                    # Add assistant response to chat state so it persists on reload
                    st.session_state.messages.append({"role": "assistant", "content": result["answer_text"]})

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")