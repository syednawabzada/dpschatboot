import streamlit as st
import google.generativeai as genai

# ---------------------------
# 🔑 Configure Gemini API key
# ---------------------------
genai.configure(api_key="AIzaSyBEk9M_ZiFjwnu6bcJFU62YWAQa-K8VsI4")

AVAILABLE_MODELS = ["gemini-2.0-flash", "gemini-2.0-pro"]

# ---------------------------
# ⚙️ Streamlit page setup
# ---------------------------
st.set_page_config(page_title="DPS AI Chatbot", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    .stChatMessage {border-radius: 15px; padding: 8px;}
    .stApp {background-color: #0E1117; color: white;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 DPS AI Chatbot")
st.caption("Built by Digital Premier Solution • Powered by Gemini API")

# ---------------------------
# 🧠 Sidebar settings
# ---------------------------
st.sidebar.header("⚙️ Settings")
selected_model = st.sidebar.selectbox("Choose Model", AVAILABLE_MODELS)
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# ---------------------------
# 💬 Chat history setup
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hey there 👋 I'm your AI assistant. How can I help today?"}]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# 💭 Chat input
# ---------------------------
if prompt := st.chat_input("Type your message..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        model = genai.GenerativeModel(selected_model)
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
