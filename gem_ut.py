import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def inter_ques(category, difficulty):
    prompt = f"Generate a {difficulty} level {category} interview question."
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

def inter_ans(question, answer):
    prompt = f"""Evaluate the following response:\n
    Question: {question}
    Answer: {answer}\n
    Provide a score out of 10 and constructive feedback."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()
