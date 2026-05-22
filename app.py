import streamlit as st
import requests

st.set_page_config(
    page_title="FastAPI Knowledge Base",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

topics = {
    "🚀 Getting Started": [
        "What is FastAPI?",
        "How do I install FastAPI?",
        "How do I create my first endpoint?",
        "How do I run a FastAPI app?",
    ],
    "🔗 Endpoints & Routing": [
        "How do I create a GET endpoint?",
        "How do I create a POST endpoint?",
        "How do I add path parameters?",
        "How do I add query parameters?",
    ],
    "📦 Data & Validation": [
        "What is a Pydantic model?",
        "How do I validate request data?",
        "How do I return a JSON response?",
        "How do I handle optional fields?",
    ],
    "🔒 Auth & Errors": [
        "How do I handle errors in FastAPI?",
        "How do I add authentication?",
        "What is dependency injection?",
        "How do I return HTTP status codes?",
    ],
}

# Sidebar
with st.sidebar:
    st.title("📚 FastAPI Knowledge Base")
    st.markdown("---")
    st.markdown("### Browse by topic")
    topic = st.radio("", list(topics.keys()))
    st.markdown("---")
    st.caption("Powered by LlamaIndex + Groq + ChromaDB")
    st.caption("alexcomanwip project 01")



# Main area
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("## Ask anything about FastAPI")
    st.markdown(" ")

    suggested = st.selectbox(
        "Frequently asked",
        ["Select a question..."] + topics[topic]
    )

    question = st.text_area(
        "Your question",
        value=suggested if suggested != "Select a question..." else "",
        height=100
    )

    ask = st.button("Ask →", use_container_width=True, type="primary")

    if ask and question and question != "Select a question...":
        with st.spinner("Searching documentation..."):
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )
            answer = response.json()["answer"]

        st.markdown("---")
        st.markdown("### Answer")
        st.success(answer)

        with st.expander("📋 Copy as plain text"):
            st.code(answer, language=None)