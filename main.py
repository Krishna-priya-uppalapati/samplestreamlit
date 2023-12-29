import streamlit as st
#from PTL import Images
st.write("<h1>this is my streamlit<h1>",unsafe_allow_html=True)
st.write("<h1 style='color:red'>this is my streamlit<h1>",unsafe_allow_html=True)
st.file_uploader("upload a file")
st.image("https://rukminim1.flixcart.com/flap/64/64/image/69c6589653afdb9a.png?q=100")
st.video("https://www.youtube.com/watch?v=YZieL0izb2Y")
img=st.file_uploader("uploader img")
st.image(img)
