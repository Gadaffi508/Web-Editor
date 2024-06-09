#<------------------------------------------------------------------------------------------------------------------------------------------->
# Kullanılacak Kütüphaneleri import etme
# --pip install streamlit
# --pip install opencv-python
# --pip install numpy
# --pip install h5py
# --pip install pillow
# --pip install tensorflow
#<------------------------------------------------------------------------------------------------------------------------------------------->
import streamlit as st
import cv2
import numpy as np
import h5py
from PIL import Image
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Duygu tanıma modelini yükleme
# Model yüklemek için dosyadaki emotion_model dosyasının yolunu alıp buraya yapıştırmak gerekicek
#<------------------------------------------------------------------------------------------------------------------------------------------->
model_path = r'C:\Users\yusuf\OneDrive\Masaüstü\WebEditörü\Web-Editor\Work\emotion_model.hdf5'
try:
    with h5py.File(model_path, 'r') as f:
        print("Dosya başarıyla açıldı.")
except OSError as e:
    print(f"Dosya açılamadı: {e}")

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Modeli compile etmeden yükleyin
#<------------------------------------------------------------------------------------------------------------------------------------------->
emotion_model = load_model(model_path, compile=False)

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Yeni bir optimizer ile modeli compile edin
#<------------------------------------------------------------------------------------------------------------------------------------------->
emotion_model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Streamlit başlığı
#<------------------------------------------------------------------------------------------------------------------------------------------->
st.title("According to Your Feeling")
st.header('Welcome to the Game', divider='rainbow')
st.caption('Activate your camera. Automatically it attracts you.')

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Kullanıcıdan genişlik ve yükseklik değerlerini al
#<------------------------------------------------------------------------------------------------------------------------------------------->
height = st.number_input('Oyun yüksekliği:', min_value=100, max_value=1080, value=600)

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Kamerayı açma
#<------------------------------------------------------------------------------------------------------------------------------------------->
cap = cv2.VideoCapture(0)

#<------------------------------------------------------------------------------------------------------------------------------------------->
# OpenCV'den kareleri okuma ve Streamlit'te gösterme
#<------------------------------------------------------------------------------------------------------------------------------------------->
if cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.write("Kameradan görüntü alınamıyor.")
        cap.release()
else:
    st.write("Kamera açılmadı.")

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Frame'i gri tonlamalı hale getirme
#<------------------------------------------------------------------------------------------------------------------------------------------->
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Yüz tespiti
#<------------------------------------------------------------------------------------------------------------------------------------------->
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

predicted_emotion = None

for (x, y, w, h) in faces:
    #<------------------------------------------------------------------------------------------------------------------------------------------->
    # Yüzü kırpma
    #<------------------------------------------------------------------------------------------------------------------------------------------->
    roi_gray = gray[y:y+h, x:x+w]
    roi_gray = cv2.resize(roi_gray, (64, 64))
    img_pixels = keras_image.img_to_array(roi_gray)
    img_pixels = np.expand_dims(img_pixels, axis=0)
    img_pixels /= 255

    #<------------------------------------------------------------------------------------------------------------------------------------------->
    # Duygu sınıflandırması
    #<------------------------------------------------------------------------------------------------------------------------------------------->
    predictions = emotion_model.predict(img_pixels)
    max_index = np.argmax(predictions[0])
    emotions = ('Kızgın', 'İğrenme', 'Korku', 'Mutlu', 'Üzgün', 'Şaşkın', 'Doğal')
    predicted_emotion = emotions[max_index]
    #<------------------------------------------------------------------------------------------------------------------------------------------->
    # Kamerada yüzü çizme ve duygu etiketini ekleme
    #<------------------------------------------------------------------------------------------------------------------------------------------->
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Kameradan çekilen görüntüyü Streamlit uygulamasına gönderme
#<------------------------------------------------------------------------------------------------------------------------------------------->
st.image(frame, channels="BGR")

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Tespit edilen duygu durumuna göre oyun yönlendirmesi
#<------------------------------------------------------------------------------------------------------------------------------------------->
if predicted_emotion:
    st.write(f"Harika! Sen çok {predicted_emotion}. Şimdi bir oyun oynamaya ne dersiniz?")
    
    if predicted_emotion == 'Kızgın':
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/cartoon-network-karakter-matik/oyna"
    elif predicted_emotion == 'İğrenme':
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/teen-titans-go-titanlar-birligi/oyna"
    elif predicted_emotion == 'Korku': 
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/gumball-ruyadan-kac%C4%B1s/oyna"
    elif predicted_emotion == 'Mutlu':
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/teen-titans-go-yildizlar-karmasi/oyna"
    elif predicted_emotion == 'Üzgün':
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/cartoon-network-masa-hokeyi-kapismasi/oyna"
    elif predicted_emotion == 'Şaşkın':
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/sevimli-kahramanlar-hikayeler-topac-taz/oyna"
    elif predicted_emotion == 'Doğal':
        game_url = "https://www.cartoonnetwork.com.tr/oyunlar/kafadar-ayiciklar-tapinak-ayilari/oyna"

    st.markdown(f"### Oynamak için aşağıdaki oyunu kullanabilirsiniz!")

    #<------------------------------------------------------------------------------------------------------------------------------------------->
    # Yönlendirilen oyunun Pozisyonlarını ayarlama
    #<------------------------------------------------------------------------------------------------------------------------------------------->
    st.markdown(
        f'''
        <style>
        .iframe-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        .iframe-container iframe {{
            width: 1080px;
            height: {height}px;
            border: none;
        }}
        </style>
        <div class="iframe-container">
            <iframe src="{game_url}"></iframe>
        </div>
        ''', 
        unsafe_allow_html=True
    )

#<------------------------------------------------------------------------------------------------------------------------------------------->
# Kamerayı kapatma
#<------------------------------------------------------------------------------------------------------------------------------------------->
cap.release()
