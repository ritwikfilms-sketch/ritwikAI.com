import streamlit as st

st.set_page_config(page_title="Ritwik AI", page_icon="🤖")

st.title("🤖 Ritwik AI")

st.write("Welcome to Ritwik AI platform")

question = st.text_input("Ask anything")

if question:
    st.write("You asked:", question)
