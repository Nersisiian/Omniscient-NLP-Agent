import streamlit as st

st.title('Omniscient NLP Agent Dashboard')
st.write('Мониторинг запросов и метрик модели')
query = st.text_input('Введите вопрос')
if st.button('Отправить'):
    import asyncio
    import nest_asyncio
    from api.main import query_nlp
    from api.main import Query
    nest_asyncio.apply()
    response = asyncio.run(query_nlp(Query(text=query)))
    st.write(f"Ответ: {response['answer']}")
    st.write(f"Контекст: {response['context']}")