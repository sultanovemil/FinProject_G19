import streamlit as st

st.set_page_config(page_title="Student Assistant")

st.markdown(' # :female-student: Персональный помощник для студентов')
st.markdown('## Введение')
st.markdown('''**Общая цель проекта** заключается в облегчении процесса изучения английского языка 
и помощи студентам достичь более эффективных результатов в учебе.''')
st.markdown('''**Цель проекта** состоит в создании инструмента,
который поможет студентам в изучении английского языка.''')
st.markdown('**Основные задачи проекта**')
st.markdown('''1. Создать простой и интуитивно понятный интерфейс.''')
st.markdown('''2. Разработать инструмент для создания карточек, который поможет студентам запоминать английские слова и их 
значения с помощью ассоциаций и примеров.''')
st.markdown('''3. Предоставить возможность студентам 
создавать структурированные конспекты текстов на английском языке, чтобы облегчить изучение и запоминание информации.''') 
st.markdown('''4. Обеспечить интерактивный и творческий подход к изучению английского языка посредством описания сгенерированных изображений.''')
st.markdown('## Анализ проблемы')
st.markdown('''**Текущая ситуация.** Студенты, обучающиеся по специальности "Инженерия 
машинного обучения", сталкиваются с рядом проблем и ограничений в 
процессе изучения английского языка. 
            
В области машинного обучения существует 
множество технических терминов на английском языке, которые 
могут вызвать сложности в запоминании у студентов. Это в свою очередь создает преграды 
при чтении научных статей, документации и других материалов на английском языке.
            
Студенты сталкиваются с ограниченным доступом к качественному контенту на 
английском языке, связанному с областью машинного обучения. Это может затруднять 
их обучение и понимание актуальных тем и разработок.''')

st.markdown('## Описание решения')
st.markdown('''Данное IT-решение предоставляет функциональность для создания конспектов текстов на английском 
языке и помощь в изучении английских слов с использованием карточек и визуальных образов.''')
st.markdown('''**План реализации**
1. Изучить потребности студентов и определить основные функциональные возможности приложения.
2. Разработать архитектуру и выбрать технологии для реализации проекта.
3. Разработать API, используя модели Huggingface, для создания конспектов текстов на английском 
языке, генерирования и перевода текста на английском языке, генерирования изображений по ключевым словам. 
4. Интегрировать модули и провести тестирование приложения. Оценить и улучшить систему. 
5. Разместить файлы на GitHub и развернуть приложение на платформе Hugging Face. 
6. Оформить документацию. Создать презентацию проекта.     
''')
st.markdown('''**Технологии, инструменты**
1. Streamlit. Этот инструмент позволяет создавать интерактивные веб-приложения с помощью Python.
2. API для Hugging Face моделей (BART, Helsinki-NLP, Stable-diffusion и Blenderbot)
3. Hugging Face Spaces - это платформа, которая позволяет создавать, 
размещать и обмениваться моделями, датасетами и блокнотами. 
4. GitHub - это платформа разработки программного обеспечения, 
которая предоставляет систему контроля версий и возможность совместной работы над проектами.
''')
st.markdown('## Практическая ценность и применимость')
st.markdown('''Это приложение поможет студентам улучшить образовательный процесс, предоставляя персонального помощника, 
который будет автоматически составлять конспекты текстов на английском языке. Cтуденты получат возможность улучшить творческие способности, навыки 
восприятия, описания изображений и понимания английского языка через визуальное обучение. Кроме того, приложение будет 
помогать студентам учить английские слова посредством использования карточек, что позволит им эффективно 
запомнить новую лексику и улучшить свои навыки в английском языке.''')
st.markdown('## Команда и план действий')
st.markdown('''
+ Болотов М.
+ Гилёв Д.
+ Пахомов Д.
+ Шибакова А.
+ Султанов Э.
''')
st.markdown('**Роли и этапы реализации проекта**')
with st.chat_message("user"):                  
    st.markdown('Шибакова А.')
    st.markdown('Изучение потребностей студентов и определение основных функциональных возможностей системы.')
with st.chat_message("assistant"):                  
    st.markdown('Болотов М.')
    st.markdown('Разработка архитектуры и выбор технологий для реализации проекта.')
with st.chat_message("assistant"):                  
    st.markdown('Гилёв Д., Пахомов Д.')
    st.markdown('Разработать API, используя модели Huggingface, для создания конспектов текстов на английском языке, генерирования и перевода текста на английском языке, генерирования изображений по лючевым словам.')
with st.chat_message("user"):                  
    st.markdown('Болотов М., Гилёв Д., Пахомов Д., Шибакова А., Султанов Э.')
    st.markdown('Интеграция модулей и тестирование. Оценка и улучшение системы.')
with st.chat_message("assistant"):                  
    st.markdown('Султанов Э.')
    st.markdown('Размещение файлов на GitHub и развертываниеь приложения на платформе Hugging Face. ')
with st.chat_message("user"):                  
    st.markdown('Шибакова А.')
    st.markdown('Оформление документации. Создание презентации проекта.')
st.markdown('## Заключение')
st.markdown('''**Основные достижения и преимущества нашего решения**
1. Автоматическое составление конспектов: приложение позволяет студентам сэкономить время и усилия, 
предоставляя автоматически созданные конспекты текстов на английском языке. 
Это помогает в изучении и запоминании материала более эффективно.
2. Интерактивное обучение: путем использования карточек для изучения английских слов, 
приложение создает интерактивную и эффективную среду для улучшения словарного запаса студентов. 
Это помогает учащимся запоминать новые слова и применять их в контексте.
3. Улучшение языковых навыков: решение помогает студентам улучшить свои языковые навыки, 
включая понимание текста на английском языке, активное использование новых слов и умение составлять конспекты. 
Это дает студентам уверенность и полезные навыки для дальнейшего образования и карьеры.
**Практическая ценность и потенциал** для улучшения образовательного процесса заключаются в том, 
что наше решение предоставляет инновационный подход к изучению английского языка и созданию конспектов. 
Оно помогает студентам эффективно использовать свое время, повысить свою академическую успеваемость и 
развивать важные навыки для будущей карьеры.
''')

st.divider()