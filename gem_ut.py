import google.generativeai as genai
import streamlit as st
import time

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")

def safe_generate(prompt, retries=3, delay=3):
    for attempt in range(retries):
        try:
            time.sleep(delay)
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            if "ResourceExhausted" in str(e):
                time.sleep(20)
            else:
                raise e
    return

def inter_ques(category, difficulty):
    prompt = f"Give a {difficulty} {category} interview question."
    return safe_generate(prompt)

def inter_ans(question, answer):
    prompt = (
        f"Evaluate this interview answer:\n"
        f"Q: {question}\n"
        f"A: {answer}\n"
        f"Score out of 10 and provide concise feedback."
        f"Make sure to include the correct answer in the response."
    )
    return safe_generate(prompt)