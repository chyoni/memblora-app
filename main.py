import streamlit as st

pages = {
    "Memblora": [
        st.Page("pages/chat.py", title="Chat"),
        st.Page("pages/upload_blog.py", title="Upload Blog Files")
    ]
}

pg = st.navigation(pages)
pg.run()


