import streamlit as st
import requests
import os

# API для составления коспекта текста с использованием модели "bart-large-cnn"
API_URL_sum = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": os.getenv("api_token")}

# Функция для составления конспекта
def make_summary(payload):
	response = requests.post(API_URL_sum, headers=headers, json=payload)
	return response.json()

st.markdown('# :female-student: Персональный помощник для студентов')
st.divider()
st.markdown('# :blue_book:  Конспект на английском языке')
st.markdown('## Введите текст на английском')
full_text = st.text_area(':book:', height=300, value='Введите свой текст на английском языке')

summary_button = st.button('Составить конспект')

if summary_button:
    # Отправляем запросы через API для получения перевода слов и генерирования предложений
    with st.spinner('...'):
        summary_text = make_summary({"inputs": full_text})
        with st.expander("Конспект"):
            st.write(summary_text[0]['summary_text'])   
        st.success('Готово')

st.divider()