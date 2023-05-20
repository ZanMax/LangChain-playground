from chat import run_llm
import streamlit as st
from streamlit_chat import message

st.title("Docs to Chat AI")
st.header("Docs to Chat AI")

prompt = st.text_input("Enter your question here")

if prompt:
    response = run_llm(prompt)

    formatted_response = f'{response["result"]}'
    message(formatted_response)
