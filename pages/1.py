import streamlit as st
with st.echo():
    name=st.text_input("이름?")
    if st.button("저장"):
        st.write(f"{name}안녕")
        st.session_state["이름"]=name
        #st.session_state.이름=name