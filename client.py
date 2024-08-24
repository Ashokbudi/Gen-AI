import streamlit as st
import requests


def e_request(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input":{"topic":input_text}}
    )
    return response.json()["output"]

def p_request(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input":{"topic":input_text}}
    )
    
    return response.json()["output"]

st.title("MY API CLIENT")
e_input = st.text_input("enter the essay topic you want")
e_button = st.button("click here for your essay")

p_input = st.text_input("enter the poem topic you want")
p_button = st.button("click here for your poem")

if e_input and e_button:
    output=e_request(e_input)
    st.write(output)
if p_input and p_button:
    outputt=p_request(p_input)
    st.write(outputt)