import streamlit as st
import requests
import io
from PIL import Image, UnidentifiedImageError
import os
import time

st.set_page_config(page_title="Student Assistant")

# API для генерации изображения
API_URL_img = "https://api-inference.huggingface.co/models/playgroundai/playground-v2-1024px-aesthetic"
headers = {"Authorization": os.getenv("api_token")}

# Функция генерации изображения
def generate_img(payload):
    response = requests.post(API_URL_img, headers=headers, json=payload)
    body = response.json()
    if 'error' in body:
        if 'estimated_time' in body:
            time.sleep(body['estimated_time'])
        else:
            print(body)
            return
        generate_img(payload)
    return response.content


st.markdown('# :female-student: Персональный помощник для студентов')
st.divider()
st.markdown("# :sparkles: Изучение английского языка через визуальное восприятие")

image_idea = st.text_input('Предложите свою тему для генерации изображения', value="Astronaut riding a horse")
image_gen__btn = st.button('Генерировать изображение')
if image_gen__btn:
    with st.spinner('...'):
        try:
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
        except UnidentifiedImageError:  
            st.warning('This is a warning', icon="⚠️")
           

st.divider()