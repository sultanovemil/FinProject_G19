import streamlit as st
import pandas as pd
import requests
import word2emoji
import os 

# Установка API URL и заголовков
API_URL_gen = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_URL_tra = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"

headers = {"Authorization": os.getenv("api_token")}

# Функция для генерирования предложения
def generate_example(payload):
	response = requests.post(API_URL_gen, headers=headers, json=payload)
	return response.json()

# Функция для перевода слова
def translate_word(payload):    
	response = requests.post(API_URL_tra, headers=headers, json=payload)
	return response.json()

# Настраеваем заголовок и название страницы
st.set_page_config(layout="wide", page_title="Students' Personal Assistant")
st.markdown(' # :female-student: Персональный помощник для студентов')
st.divider()
st.markdown('## :flower_playing_cards: Карточки для изучения английских слов')

st.sidebar.markdown('# :bookmark_tabs: :bookmark_tabs:  :bookmark_tabs:  :bookmark_tabs: ')
words_from_tarea = st.sidebar.text_area('Напиши список слов на английском', value='cat dog duck')
button_start = st.sidebar.button('Создать карточки')

cards_list = list()
if button_start:
    words_list = words_from_tarea.split()
    st.divider()
   
    
    # Отправляем запросы через API для получения перевода слов и генерирования предложений
    with st.spinner('...'):
        for word in words_list:
            example = generate_example({"text": word})
            translated = translate_word({"inputs": word})
            cards_list.append([word, translated[0]['translation_text'].lower(), example['generated_text']])
        
        # Преобразуем полученные данные в DataFrame
        cards_df = pd.DataFrame(cards_list, columns=['word', 'translated', 'example'])
    st.sidebar.success('Готово')

    # Выводим карточки 
    for el in cards_list:
        with st.chat_message("assistant"):
            #st.divider()            
            st.markdown(f'# {word2emoji(el[0])}')
            st.markdown(f'#  :red[{el[0]}]')
            st.markdown(f'## :blue[{el[1]}]')
            st.markdown(f'*        {el[2]}')
            st.divider()
    