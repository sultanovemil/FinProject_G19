import os
import time
import re

import streamlit as st
import pandas as pd
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Установка API URL и заголовков
API_URL_TRA = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"
API_URL_KEY = "https://api-inference.huggingface.co/models/ml6team/keyphrase-extraction-kbir-inspec"
API_URL_SUM = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

TOKEN = os.getenv('API_TOKEN')
headers = {"Authorization": TOKEN}


# Функция для получения ключевых слов
def get_key_words(payload):
    response = requests.post(API_URL_KEY, headers=headers, json=payload)
    body = response.json()
    if 'error' in body:
        if 'estimated_time' in body:
            time.sleep(body['estimated_time'])
        else:
            print(body)
            return
        get_key_words(payload)
    return body

# Функция для перевода слова
def translate_key_words(payload):
    response = requests.post(API_URL_TRA, headers=headers, json=payload)
    body = response.json()
    if 'error' in body:
        if 'estimated_time' in body:
            time.sleep(body['estimated_time'])
        else:
            print(body)
            return
        translate_key_words(payload)
    return body

# Функция для составления конспекта
def make_summary(payload):
    response = requests.post(API_URL_SUM, headers=headers, json=payload)
    body = response.json()
    if 'error' in body:
        if 'estimated_time' in body:
            time.sleep(body['estimated_time'])
        else:
            print(body)
            return
        make_summary(payload)
    return body


# Очищаем список слов
def clean_list(words_list):
    cleaned_words_list = []
    for word in words_list:
        word = word.lower()
        word = re.sub(r"[^а-яА-Яa-zA-Z\s]", "", word)
        word = word.lstrip()
        word = word.rstrip()
        cleaned_words_list.append(word)
    return cleaned_words_list


# Настраиваем заголовок и название страницы
st.set_page_config(layout="wide", page_title="Students' Personal Assistant")
st.markdown(' # :female-student: Персональный помощник для студентов')

st.divider()
st.markdown('# :blue_book:  Конспект на английском языке')

col1, col2 = st.columns(2)
text_from_tarea = col1.text_area('Введите тект статьи на английском языке', key='t_area', height=500)

button_start = st.button('Обработать текст')
key_words_list = []


if button_start:
    with st.spinner('Составляем конспект...'):
        # Составляем конспект
        summary_text = make_summary({"inputs": text_from_tarea})
        col2.text_area('Конспект статьи', height=500, key='sum_area', value=summary_text[0]['summary_text'])

    with st.spinner('Получаем ключевые слова...'):
        # Извлекаем ключевые слова
        kew_words = get_key_words({"inputs": text_from_tarea})
        for key_word in kew_words:
            key_words_list.append(key_word['word'].lower())

        sorted_keywords = set(sorted(key_words_list))
        sorted_keywords = clean_list(sorted_keywords)

    with st.spinner('Переводим ключевые слова...'):
        # Переводим ключевые слова
        translated_words_dict = translate_key_words({"inputs": sorted_keywords})
        translated_words_list = [word['translation_text'] for word in translated_words_dict]

        # Создаем карточки
        cleaned_words_list_ru = clean_list(translated_words_list)
        cards_list = []
        for item1, item2 in zip(sorted_keywords, cleaned_words_list_ru):
            cards_list.append([item1, item2])

    st.success('Готово')

    with st.spinner('Создаем WordCloud...'):
        # Выводим Word Cloud
        st.set_option('deprecation.showPyplotGlobalUse', False)
        words_str = ', '.join(sorted_keywords)
        w = WordCloud(background_color="white", width=1600, height=800).generate(words_str)
        plt.imshow(w, interpolation='bilinear')
        plt.imshow(w)
        plt.axis("off")
        st.pyplot()

    # Выводим карточки
    st.markdown('# :bookmark_tabs: Карточки из ключевых слов')
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    for index, el in enumerate(cards_list):
        with columns[(index + 1) % 3]:
            with st.container(border=True):
                col4, col5 = st.columns([0.1, 0.9])
                with col4:
                    st.write("# :flower_playing_cards:")
                with col5:
                    st.write(f'## :green[{el[0]}]')
                    st.write(f'### :blue[{el[1]}]')
