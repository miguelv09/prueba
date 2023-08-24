import streamlit as st
from PIL import Image 

st.write("Mi primera aplicación")

image = Image.open('Imagen album.png')


st.image(image, caption = 'Hola Soy Lasso')
st.write("Mi primera aplicación")
