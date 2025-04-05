import streamlit as st
from gem_ut import inter_ques, inter_ans

st.set_page_config(page_title="IntelecView", layout="centered")
st.title("🤖 IntelecView AI powered Interview Question Generator & Evaluator")

st.markdown("Prepare for your interviews using AI!")

category = st.selectbox("Select Interview Category", ["Data Structures", "System Design", "HR"])
difficulty = st.radio("Select Difficulty", ["Easy", "Medium", "Hard"])

if st.button("🎯 Generate Question"):
    question = inter_ques(category, difficulty)
    st.session_state["question"] = question
    st.success("✅ Question Generated")
    st.markdown(f"**Question:** {question}")


if "question" in st.session_state:
    answer = st.text_area("Your Answer", height=200, placeholder="Type your answer here...")
    if st.button("📩 Submit Answer for Evaluation"):
        with st.spinner("Evaluating your response..."):
            feedback = inter_ans(st.session_state["question"], answer)
        st.subheader("🧠 AI Feedback")
        st.markdown(feedback)
