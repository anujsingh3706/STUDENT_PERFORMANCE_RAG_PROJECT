import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import streamlit as st
from rag.chain import RAGChatbot
from dashboard.analytics import load_data, plot_average_marks, plot_performance_counts, plot_attendance

# Init chatbot
bot = RAGChatbot()

st.set_page_config(page_title="Student RAG Chatbot", layout="wide")

st.title("🎓 Student Performance RAG Chatbot")

# Sidebar filters
st.sidebar.header("Filters")

df = load_data()

selected_class = st.sidebar.selectbox("Select Class", sorted(df["class"].unique()))
selected_perf = st.sidebar.selectbox("Select Performance", df["performance"].unique())

filtered_df = df[
    (df["class"] == selected_class) &
    (df["performance"] == selected_perf)
]

# Tabs
tab1, tab2 = st.tabs(["💬 Chatbot", "📊 Dashboard"])

# ---------------- CHATBOT ----------------
with tab1:
    st.subheader("Ask Questions")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:")

    if user_input:
        response = bot.chat(user_input)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

    for role, msg in st.session_state.chat_history:
        st.write(f"**{role}:** {msg}")

# ---------------- DASHBOARD ----------------
with tab2:
    st.subheader("Student Analytics")

    st.write("Filtered Data:", filtered_df.head())

    st.pyplot(plot_average_marks(filtered_df))
    st.pyplot(plot_performance_counts(filtered_df))
    st.pyplot(plot_attendance(filtered_df))