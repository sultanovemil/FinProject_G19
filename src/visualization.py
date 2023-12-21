import io
import json
import os
import time

from PIL import Image
import requests
import streamlit as st


# API для генерации изображения
API_URL_IMG = "https://api-inference.huggingface.co" \
              "/models/playgroundai/playground-v2-1024px-aesthetic"
API_URL_SPE = "https://api-inference.huggingface.co" \
              "/models/facebook/mms-tts-eng"

TOKEN = os.getenv('API_TOKEN')
HEADERS = {"Authorization": TOKEN}

st.set_page_config(page_title="Student Assistant")


if 'clicked_button' not in st.session_state:
    st.session_state.clicked_button = False
if 'generated_image' not in st.session_state:
    st.session_state.generated_image = None


def click_button():
    st.session_state.clicked_button = True
    st.session_state.generated_image = None


def hugging_api_request(url, payload):
    response = requests.post(url, headers=HEADERS, json=payload, timeout=120)

    if response.status_code == 500:
        st.exception(RuntimeError(f'{response} {url.split("/")[-1]}'
                                  ' is currently unavailable'))
        return
    try:
        body = response.json()
    except json.JSONDecodeError:
        return response.content

    if 'error' in body:
        print(response.status_code, body)
        if 'estimated_time' in body:
            st.info('Модель загружается. Она будет доступна '
                     f'через {body["estimated_time"]} сек.')
            time.sleep(body['estimated_time'])
        else:
            return
        hugging_api_request(url, payload)
    return body


# Функция генерации изображения
def generate_img(payload) -> io.BytesIO:
    return hugging_api_request(API_URL_IMG, payload)


def generate_speech(payload) -> io.BytesIO:
    return hugging_api_request(API_URL_SPE, payload)


st.markdown('# :female-student: Персональный помощник для студентов')
st.divider()
st.markdown("# :sparkles: Изучение английского языка"
            " через визуальное восприятие")

image_idea = st.text_input('Предложите свою тему для генерации изображения',
                           value="Astronaut riding a horse")
image_gen_btn = st.button('Генерировать изображение', on_click=click_button)
if st.session_state.clicked_button:
    if not st.session_state.generated_image:
        with st.spinner('Идёт загрузка изображения...'):
            image_bytes = generate_img({"inputs": image_idea})
            image_raw = io.BytesIO(image_bytes)
            st.success('Готово')
            st.session_state.generated_image = image_raw

    st.image(st.session_state.generated_image)
    st.markdown('## Опишите фотографию на английском языке')
    st.markdown('## План ответа поможет вам:')
    st.markdown('+ the place;')
    st.markdown('+ the action;')
    st.markdown('+ the person’s appearance;')
    st.markdown('+ whether you like the picture or not;')
    st.markdown('+ why.')
    st.markdown('Start with: “I’d like to describe this picture.'
                ' The picture shows …” ')
    st.divider()

    description_text = st.text_area(
        'Описание фотографии',
        key='t_area', height=250,
        placeholder=(
            'I’d like to describe this picture.'
            ' The picture shows …'))

    tts_gen_btn = st.button('Произнести текст')
    if tts_gen_btn and description_text:
        with st.spinner('Идёт загрузка аудио...'):
            audio_bytes = generate_speech({
                "inputs": description_text
            })
            if isinstance(audio_bytes, bytes):
                st.audio(audio_bytes, format='audio/ogg')
            else:
                st.warning('Что-то пошло не так, попробуйте еще раз.')

            st.success('Готово')