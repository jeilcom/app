import streamlit as st
with st.echo():
    if st.button("불러오기"):
        if "이름" in st.session_state:
            st.write(f"{st.session_state.이름}안녕")
        else:
            st.write("1페이지부터 먼저 하세요")
            