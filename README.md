# Web Editör ve Yapay Zeka Projeleri

Bu depo, üniversitedeki web editör dersimiz kapsamında yaptığımız çeşitli projeleri içermektedir. Bu projeler, veri alma, görüntü işleme, yapay zeka uygulamaları ve daha fazlasını içermektedir. Aşağıda her proje için detaylı açıklamalar ve kurulum talimatları bulabilirsiniz.

## Projeler

### 1. Veri Alma ve Görüntüleme

Bu proje, bir web sitesinden veri alıp bu veriyi kullanıcıya gösteren bir uygulamayı içerir.

#### Kullanılan Teknolojiler

- Python
- BeautifulSoup (Web Scraping)
- Flask (Web Framework)

#### Kurulum ve Kullanım

1. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2. Uygulamayı başlatın:
    ```bash
    python app.py
    ```

3. Tarayıcınızdan `http://127.0.0.1:5000/` adresine giderek uygulamayı kullanın.

### 2. Kamera ve Video Üzerine Efekt Ekleme

Bu proje, bir kameradan alınan görüntülere ve videolara efekt ekleyen bir uygulamayı içerir.

#### Kullanılan Teknolojiler

- Python
- OpenCV
- Flask (Web Framework)

#### Kurulum ve Kullanım

1. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2. Uygulamayı başlatın:
    ```bash
    python app.py
    ```

3. Tarayıcınızdan `http://127.0.0.1:5000/` adresine giderek kameranızı açın ve efektleri uygulayın.

### 3. Streamlit ve Google API ile Yapay Zeka Uygulaması

Bu proje, bir internet sitesine yüklenen fotoğrafları yorumlayan bir yapay zeka uygulamasını içerir. Google API kullanılarak görsel tanıma yapılmaktadır.

#### Kullanılan Teknolojiler

- Python
- Streamlit
- Google Cloud Vision API

#### Kurulum ve Kullanım

1. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2. Google Cloud Vision API anahtarınızı `config.py` dosyasına ekleyin:
    ```python
    GOOGLE_CLOUD_VISION_API_KEY = 'your_api_key_here'
    ```

3. Uygulamayı başlatın:
    ```bash
    streamlit run app.py
    ```

4. Tarayıcınızdan `http://localhost:8501` adresine giderek fotoğraf yükleyin ve yapay zeka yorumlarını görün.

## Katkıda Bulunma

Eğer projelere katkıda bulunmak isterseniz, lütfen bir `pull request` gönderin veya bir `issue` açın. Katkılarınızı memnuniyetle karşılarız.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
