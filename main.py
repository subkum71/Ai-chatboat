## Main execution
import streamlit as st
from app.Agent.agent import agent

st.set_page_config(
    page_title="E-Commerce AI Assistant",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 E-Commerce AI Assistant")
st.caption("Powered by LangChain + Ollama")
st.write("How can I help you")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("Chat")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []
# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# -----------------------------
# User Input
# -----------------------------

user_input = st.chat_input(
    "Ask about your order, check products or categories..."
)


if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # -----------------------------
    # Calling Agent
    # -----------------------------
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = agent.invoke({
                "messages": st.session_state.messages
            })

            answer = response["messages"][-1].content

            st.markdown(answer)
    # -----------------------------
    # Save Response
    # -----------------------------
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })