#pip install streamlit
#streamlit run 파일명
#streamlit run home.py


import streamlit as st
#count=1
#print(count)
st.title('데이터분석')


st.header("데이터분석_ is :red[Hot] :1234:")
st.header("파이썬 기초", divider="gray")
st.header("자료구조", divider=True)
st.header("제어문", divider=True)
st.header("Numpy", divider=True)
st.header("Pandas", divider=True)
st.header("Matplotlib", divider=True)
with st.echo():
    a=3
    b=7
    st.write(f'{a}+{b}={a+b}')
    st.write('This code will be printed')


with st.echo():
    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")