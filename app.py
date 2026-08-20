import streamlit as st
from PIL import Image
st.title ("hola!!, mi nombre es princesita")

image= Image.open("amoor.jpg")
st.image (image,caption = "momeypablo")

st.header("pagina de salome y pablo")
st.write ("somos los novios mas lindos del mundo")
