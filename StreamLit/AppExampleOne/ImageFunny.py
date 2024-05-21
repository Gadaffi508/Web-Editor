import streamlit as st
import cv2
from PIL import Image

st.title("Görsel Düzenleyici")

data = st.file_uploader("Resim Yükle")
if data:
    image = Image.open(data)
    image.save('uploaded_image.png')
    st.image("uploaded_image")
image = cv2.imread("uploaded_image.png")