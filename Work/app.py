import streamlit as st
from PIL import Image
import requests

# Yüz tanıma kütüphanesi
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.models import load_model

# Duygu tanıma modelini yükleme
emotion_model = load_model('path_to_your_emotion_model')

# Streamlit başlığı
st.title("Hoşgeldiniz!")

# Kamerayı açma
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Frame'i gri tonlamalı hale getirme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Yüzü kırpma
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = keras_image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        # Duygu sınıflandırması
        predictions = emotion_model.predict(img_pixels)
        max_index = np.argmax(predictions[0])
        emotions = ('Kızgın', 'İğrenme', 'Korku', 'Mutlu', 'Üzgün', 'Şaşkın', 'Doğal')
        predicted_emotion = emotions[max_index]

        # Kamerada yüzü çizme ve duygu etiketini ekleme
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Kameradan çekilen görüntüyü Streamlit uygulamasına gönderme
    st.image(frame, channels="BGR")

    # Streamlit üzerinden duygu durumunu kontrol etme
    if predicted_emotion == 'Mutlu':
        st.write("Harika! Sen çok mutlusunuz. Şimdi bir oyun oynamaya ne dersiniz?")
        # Burada mutlu olduğunda yönlendireceğiniz oyunu başlatmak için gerekli kodları ekleyebilirsiniz.
        break
    elif predicted_emotion == 'Üzgün':
        st.write("Üzgün görünüyorsunuz. Belki bir oyun oynamak moralinizi yükseltir.")
        # Burada üzgün olduğunda yönlendireceğiniz oyunu başlatmak için gerekli kodları ekleyebilirsiniz.
        break

# Kamerayı kapatma
cap.release()
