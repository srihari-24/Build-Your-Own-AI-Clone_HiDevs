import streamlit as st
import google.generativeai as genai
import os

# ==== PASTE YOUR GEMINI API KEY HERE! ====
api_key = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"

# ------------------------------------------
st.set_page_config(page_title="AI Clone", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
        .main {background-color: #18181b;}
        .stApp {background-color: #18181b;}
        .stTextInput>div>div>input {background-color: #28283a; color: #fafafa;}
        .stButton>button {background-color: #4949e7; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Build Your Own AI Clone")
st.markdown("Ask anything, get smart, helpful answers!")

# Set up Gemini API
genai.configure(api_key=GENAI_API_KEY)

# -- Load FAQ file (if available) --
faq_file = "faq.txt"
def load_faq():
    if os.path.exists(faq_file):
        with open(faq_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

faq_data = load_faq()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown("### 💬 Ask a question:")

user_q = st.text_input("Type your question...", key="user_input")
ask_btn = st.button("Ask")

if ask_btn and user_q.strip():
    prompt = "You are a helpful assistant. Use the FAQ below if helpful. If not, answer as best as you can.\n\n"
    if faq_data:
        prompt += f"FAQ:\n{faq_data}\n\n"
    prompt += f"User: {user_q}\nAssistant:"
    with st.spinner("Thinking..."):
        try:
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            resp = model.generate_content(prompt)
            ai_answer = resp.text.strip()
        except Exception as e:
            ai_answer = f"Error: {e}"

    st.session_state.chat_history.append({"user": user_q, "ai": ai_answer})

# Show chat history
for msg in st.session_state.chat_history[::-1]:
    with st.chat_message("user"):
        st.markdown(msg["user"])
    with st.chat_message("ai"):
        st.markdown(msg["ai"])

st.markdown("---")
