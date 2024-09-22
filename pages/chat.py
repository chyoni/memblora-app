import requests
import streamlit as st

st.set_page_config(page_title="Memblora", page_icon="🌈")

st.title("Memblora")
st.caption("내가 작성했던 블로그 포스팅이 기억나지 않을때, Memblora에게 물어보세요!")

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if user_question := st.chat_input(placeholder="블로그 제목을 찾기 위해 단서와 함께 질문해보세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})
    with st.spinner("답변을 생성하는 중입니다"):
        params = {'query': f'{user_question}'}
        ai_response = requests.get("http://localhost:8000/llm/query", params=params).json()

        with st.chat_message("ai"):
            ai_message = st.write(ai_response['memblora'])
            st.session_state.message_list.append({"role": "ai", "content": ai_response['memblora']})