import streamlit as st
st.write("<h1>this is my streamlit<h1>",unsafe_allow_html=True)
st.write("<h1 style='color:red'>this is my streamlit<h1>",unsafe_allow_html=True)
st.file_uploader("upload a file")
st.image('jpg','png','jpeg')
