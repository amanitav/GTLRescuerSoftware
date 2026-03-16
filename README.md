# GTLYazılım: Afet Bölgesi Analiz ve Haritalama Sistemi

Afet ekiplerinin deprem sonrasında İHA'lar ile elde edilen ham görüntüleri işleyerek, anlamlı ve coğrafi bir harita katmanına dönüştüren bir yazılım çözümüdür.

## Vizyonumuz
Afet sonrası hızlı ve doğru karar alma süreçlerini desteklemek adına;
- **Koordinasyon:** Ekiplerin planlı ilerlemesini sağlamak.
- **Hız:** Enkaz tespiti ve bölge analizini yapay zeka ile otomatikleştirmek.
- **Şeffaflık:** İşlenen verileri etkileşimli haritalar üzerinden sahadaki ekiplere sunmak.

## Proje Özellikleri
- **Enkaz Tespiti:** Kendi oluşturduğumuz 41 bin fotoğraflı özgün datasetimiz ile yolov8m modelini eğittik ortaya çıkan modeli enkaz tespitinde kullandık
- **Akıllı Haritalama:** Rasperry pi ile çektiğimiz fotoğrafların koordinat verilerine dayalı, birleştirilmiş mozaik harita katmanları.
- **Arayüz:** Streamlit tabanlı interaktif kontrol paneli ve geliştireceğimiz mobil intrnetsiz uygulamamız.
- **Veri Analitiği:** Tespit edilen enkazların anlık istatistiksel raporlanması, afet ekiplerine sunulması

---
*Projemizin detaylarını incelemek isterseniz kodlarımızı inceleyebilirsiniz.*

## Projeyi Nasıl Çalıştırırım?
1. Afet_Analiz_Sistemi.py dosyasını bulun ve Bilgisiyarınıza kodları kopyalayın.
2. Gerekli kütüphaneleri yükleyin: `pip install ultralytics streamlit folium streamlit-folium opencv-python`
3. Terminale şu kodu yazın: `streamlit run Afet_Analiz_Sistemi.py`

