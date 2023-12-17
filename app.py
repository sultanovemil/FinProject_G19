import streamlit as st
import pandas as pd
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os 
import re

# Установка API URL и заголовков
API_URL_tra = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"
API_URL_key = "https://api-inference.huggingface.co/models/ml6team/keyphrase-extraction-kbir-inspec"
API_URL_sum = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": os.getenv("api_token")}


# Функция для получения ключевых слов
def get_key_words(payload):
	response = requests.post(API_URL_key, headers=headers, json=payload)
	return response.json()

# Функция для перевода слова
def translate_key_words(payload):
	response = requests.post(API_URL_tra, headers=headers, json=payload)
	return response.json()

# Функция для составления конспекта
def make_summary(payload):
	response = requests.post(API_URL_sum, headers=headers, json=payload)
	return response.json()


# Очищаем список слов
def clean_list(words_list):
    cleaned_words_list = []
    for word in words_list:
        word = word.lower()
        word =re.sub(r"[^а-яА-Яa-zA-Z\s]", "", word)
        word = word.lstrip()
        word = word.rstrip()
        cleaned_words_list.append(word)
    return cleaned_words_list


# Настраеваем заголовок и название страницы
st.set_page_config(layout="wide", page_title="Students' Personal Assistant")
st.markdown(' # :female-student: Персональный помощник для студентов')

st.divider()
st.markdown('# :blue_book:  Конспект на английском языке')



col1, col2 = st.columns(2)
text_from_tarea = col1.text_area('Введите тект статьи на английском языке', height=500)


button_start = st.button('Обработать текст')

key_words_list = []
if button_start:
    
    with st.spinner('...'):
        # Составляем конспект
        summary_text = make_summary({"inputs": text_from_tarea})
        col2.text_area('Конспект статьи', height=500, value=summary_text[0]['summary_text']) 
        
        # Извлекаем ключевые слова
        kew_words = get_key_words({	"inputs": text_from_tarea,})
        for key_word in kew_words :
            key_words_list.append(key_word['word'].lower())
        
        sorted_keywords = set(sorted(key_words_list))
        sorted_keywords = clean_list(sorted_keywords)

        # Переводим ключевые слова
        translated_words_list = []
        for key_word in sorted_keywords:   
            res = translate_key_words({"inputs": key_word,})
            translated_words_list.append(res[0]['translation_text'])

        # Создаем карточки
        cleaned_words_list_ru = clean_list(translated_words_list)
        cards_list = []
        for item1, item2 in zip(sorted_keywords, cleaned_words_list_ru):            
            cards_list.append([item1, item2])
        
        
    st.success('Готово')

    # Выводим Word Cloud
    st.set_option('deprecation.showPyplotGlobalUse', False)
    words_str = ', '.join(sorted_keywords)
    w = WordCloud(background_color="white").generate(words_str)
    plt.imshow(w, interpolation='bilinear')
    plt.imshow(w)
    plt.axis("off")
    st.pyplot()

    # Выводим карточки 
    st.markdown('# :bookmark_tabs: Карточки из ключевых слов')
    for el in cards_list:
        with st.chat_message("assistant"):
            #st.divider()            
            st.markdown('# :flower_playing_cards:')
            st.markdown(f'#  :green[{el[0]}]')
            st.markdown(f'## :blue[{el[1]}]')            
            st.divider()