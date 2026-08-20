import streamlit as st
from PIL import Image
st.title ("hola!!, mi nombre es princesita")

image= Image.open("amoor.jpg")
st.image (image,caption = "momeypablo")

st.header("pagina de salome y pablo")
st.write ("somos los novios mas lindos del mundo")

texto= st.text_input("aaaaaah!!!!","este es mi texto")
st.write("el texto escrito es", texto)

st.subheader("ahora usemos 2 columnas")

col1,col2= st.columns(2)
with col1:
  st.subheader("esta es la primera columna")
  st.write("las interfaces multimodales mejoran la experiencia de usuario")
  resp=st.checkbox("estoy de acuerdo")
  if resp:
    st.write("correcto")

with col2:
  st.subheader("esta es la segunda columna")
  modo=st.radio ("cual es la modalidad que predomina en tu interfaz", ("visual", "auditiva", "tactil"))
  if modo == "visual":
    st.write("lo visual es importante para las interfaces")

  if modo == "auditiva":
    st.write("la audicion es importante para las interfaces")

  if modo == "tactil":
    st.write("el tactil es importante para las interfaces")
    
  
