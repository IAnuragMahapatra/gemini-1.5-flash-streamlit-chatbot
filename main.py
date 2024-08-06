import os

import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="RAVEN",
    page_icon="💬",
    layout="centered",
)

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


st.title("RAVEN 🐦‍⬛")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask anything ...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
