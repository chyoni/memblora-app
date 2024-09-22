import requests
import streamlit as st

st.set_page_config(page_title="Upload Blog Files", page_icon="🌈")

st.title("Upload Blog Files")
st.caption("Memblora가 당신의 블로그 제목을 알려줄 수 있도록 블로그 포스팅을 심어주세요!")
st.caption("블로그 포스팅은 단일 블로그 HTML 파일 또는 HTML 파일들의 Zip 파일로 올려주세요!")

uploaded_file = st.file_uploader("Choose a HTML or HTMLs.zip file", accept_multiple_files=False)

if uploaded_file is not None:

    with st.spinner("Uploading file and processing..."):
        files = {'file': uploaded_file}
        response = requests.post("http://localhost:8000/llm/embedding", files=files)

        if response.status_code == 200:
            st.success('파일 업로드가 성공적으로 끝났습니다.')
        else:
            st.error('알수 없는 오류가 발생했습니다. 신속한 조치 중입니다. 몇분 후에 다시 시도해주세요.')


