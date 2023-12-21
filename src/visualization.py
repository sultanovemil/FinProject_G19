import streamlit as st
import requests
import io
from PIL import Image, UnidentifiedImageError
import os
import time

st.set_page_config(page_title="Student Assistant")

# API для генерации изображения
API_URL_IMG = "https://api-inference.huggingface.co/models/playgroundai/playground-v2-1024px-aesthetic"
headers = {"Authorization": os.getenv('API_TOKEN')}

# Функция генерации изображения
def generate_img(payload):
    try:
        response = requests.post(API_URL_IMG, headers=headers, json=payload)
    except json.JSONDecodeError as e:
        print("Ошибка декодирования JSON:", e)
        time.sleep(3)
        generate_img(payload)
    else:
        return response.content


st.markdown('# :female-student: Персональный помощник для студентов')
st.divider()
st.markdown("# :sparkles: Изучение английского языка через визуальное восприятие")

image_idea = st.text_input('Предложите свою тему для генерации изображения', value="Astronaut riding a horse")
image_gen__btn = st.button('Генерировать изображение')
if image_gen__btn:
    with st.spinner('Идёт загрузка изображения...'):
        image_bytes = generate_img({"inputs": image_idea}) 
        image_raw = io.BytesIO(image_bytes) 
        st.success('Готово')            
        st.image(image_raw)     
        st.markdown('## Опишите фотографию на английском языке') 
        st.markdown('## План ответа поможет вам:') 
        st.markdown('+ the place;') 
        st.markdown('+ the action;') 
        st.markdown('+ the person’s appearance;') 
        st.markdown('+ whether you like the picture or not;') 
        st.markdown('+ why.') 
        st.markdown('Start with: “I’d like to describe this picture. The picture shows …” ')
st.divider()