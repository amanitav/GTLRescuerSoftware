# GTLYazılım: Afet Bölgesi Analiz ve Haritalama Sistemi

Afet ekiplerinin deprem sonrasında İHA'lar ile elde edilen ham görüntüleri işleyerek, anlamlı ve coğrafi bir harita katmanına dönüştüren bir yazılım çözümüdür.

## Vizyonumuz
Afet sonrası hızlı ve doğru karar alma süreçlerini desteklemek adına;
- **Koordinasyon:** Ekiplerin planlı ilerlemesini sağlamak.
- **Hız:** Enkaz tespiti ve bölge analizini yapay zeka ile otomatikleştirmek.
- **Şeffaflık:** İşlenen verileri etkileşimli haritalar üzerinden sahadaki ekiplere sunmak.

## Görüntü İşleme Modeli
- **Enkaz Tespiti:** Kendi oluşturduğumuz 41 bin fotoğraflı özgün datasetimiz ile yolov8m modelini eğittik ortaya çıkan modeli enkaz tespitinde kullandık
- **Akıllı Haritalama:** Rasperry pi ile çektiğimiz fotoğrafların koordinat verilerine dayalı, birleştirilmiş mozaik harita katmanları.
- **Arayüz:** Streamlit tabanlı interaktif kontrol paneli ve geliştireceğimiz mobil intrnetsiz uygulamamız.
- **Veri Analitiği:** Tespit edilen enkazların anlık istatistiksel raporlanması, afet ekiplerine sunulması

---
*Projemizin detaylarını incelemek isterseniz aşağıdaki adımları inceleyebilirsiniz.*

## Yazılımı Nasıl Çalıştırırım?
1. Bizle İletişime geçerek model dosyalarını talep edebilirsiniz demo için sonraki adımı takip edin
2. [Afet_Analiz_Sistemi.py dosyasını bulun](https://github.com/amanitav/GTLRescuerSoftware/blob/main/Afet_Analiz_Sistemi.py) bu linke girin ve Pycharm'ınıza kodları kopyalayın.
3. Gerekli kütüphaneleri yükleyin: `pip install ultralytics streamlit folium streamlit-folium opencv-python`
4. Terminale şu kodu yazın: `streamlit run sizin o anki dosya adınız.py`
Not (Önemli): kodunuzu çalıştırdığınızda sadece uydu görüntüleri kısmını çalıştırabileceksiniz diğer yerlerde hata verecek çünkü hem fotoğraflar sizde yok hem de koddaki yolo modelimiz sizde yok ve maalesefki modelimizi sizinle paylaşamayız ama bunu telafi olarak size diğer afet haritası ve işlenmiş harita sekmelerinin fotoğrafını githuba yükledik oradan bakabilirsiniz

### Proje Ekran Görüntüleri

**Afet Haritası:**
([Afet Haritası](https://github.com/amanitav/GTLRescuerSoftware/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-03-16%20180119.png))

**İşlenmiş Harita (Enkaz Tespiti):**
([İşlenmiş Harita](https://github.com/amanitav/GTLRescuerSoftware/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-03-16%20180137.png))



## Geliştirme Süreci Hakkında Bilgilendirme
Projemiz aktif bir geliştirme sürecindedir. Şu an GitHub üzerinden paylaşılan model, 20 epochluk bir eğitim aşamasından elde edilen öncelikli prototip verileridir. Ekibimiz, enkaz tespitindeki doğruluk payını maksimize etmek adına eğitim ve optimizasyon çalışmalarına devam etmektedir.

# GTLTasarım : Özgün VTOL İHA ve Yer İstasyonu Tasarımı

## İHA Teknik Çizimi
<img width="6250" height="4419" alt="Elektronik (6)" src="https://github.com/user-attachments/assets/56b9e826-30ca-4e10-ac04-48bc7a81280c" />

## Anisopetra ile Biyomimikri

<img width="6250" height="4419" alt="Elektronik (7)" src="https://github.com/user-attachments/assets/926f3962-0445-488a-9b5f-debe2f4c19a4" />

## Taşıma Çantası ve İHA'nın Modüler Tasarımı

<img width="6250" height="4419" alt="Elektronik (8)" src="https://github.com/user-attachments/assets/c96ee556-90fb-4056-a065-d3290f1dcccb" />

## Yer İstasyonu Taşıma Çantası

<img width="6250" height="4419" alt="Elektronik (9)" src="https://github.com/user-attachments/assets/79775f5a-7921-425a-9d95-28c95a238122" />



