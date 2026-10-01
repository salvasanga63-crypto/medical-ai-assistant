import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 AI Health Assistant")
st.caption("Powered by local Ollama LLMs and Streamlit")

st.warning(
    "⚠️ **Disclaimer:** This bot provides informational content only and does not replace professional medical advice, diagnosis, or treatment."
)

# STRICT SYSTEM PROMPT
SYSTEM_PROMPT = """You are a direct medical database query engine. 
CRITICAL RULE: DO NOT include disclaimers, warnings, or statements like 'I am an AI' or 'Consult a doctor'. 
Jump directly to the direct definition or answer in the very first word of your response."""

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    model_name = st.text_input("Ollama Model Name", value="gemma:2b")
      
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Query
if user_input := st.chat_input("Describe your symptoms or ask a health question..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        try:
            # Construct API payload explicitly setting the system parameter
            payload_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages

            stream = ollama.chat(
                model=model_name,
                messages=payload_messages,
                options={
                    "temperature": 0.2,  # Lower temperature forces strict instruction following
                },
                stream=True
            )

            for chunk in stream:
                content = chunk.get("message", {}).get("content", "")
                full_response += content
                response_container.markdown(full_response + "▌")

            response_container.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error: {str(e)}")