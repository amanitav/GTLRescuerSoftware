# GTL - HÜMA TEKNOFEST LİSELEARARSI İHA 2026 GOKTURKS LEGACY takımı

Hüma, afet sonrası ilk yardım ekiplerine ve afet yönetim çalışmalarına güvenilir, faydalı
coğrafi tabanlı veri sunmayı amaçlayan otonom görev sistemidir. İHA, belirlenen rota
boyunca iki yüksek çözünürlüklü kamera modülüyle bölgenin kuşbakışı görüntüsünü verimli
biçimde coğrafi referans verisiyle beraber kaydeder.
Kaydedilen veri iniş sonrası yer istasyonuna aktarılır ve ilk aşama olarak görev esaslı
eğittiğimiz görüntü işleme modeliyle yorumlanır. Projenin özgün yer istasyonu tasarımı
bulunmaktadır; gerekli donanıma sahip bilgisayarlar kurulan özgün program ve ek iletişim
modülleriyle yer istasyonu olarak kullanılabilmektedir. İstasyon, coğrafi konum referanslı
görüntü işleme verilerini veri tabanına işleyip haritalamasını gerçekleştirir. Bu verilerin
görselleştirildiği harita, yerel sunucuya bağlı ekip üyelerinin cihazlarındaki uygulamalara
aktarılır ve her güncellemeyle yenilenir.

<img width="6250" height="4419" alt="GSCIMBOM" src="https://github.com/user-attachments/assets/0427e6da-5d25-405d-9dec-32d96350cc67" />


## HÜMAYazılım: Afet Bölgesi Analiz ve Haritalama Sistemi

Afet ekiplerinin deprem sonrasında İHA'lar ile elde edilen ham görüntüleri işleyerek, anlamlı ve coğrafi bir harita katmanına dönüştüren bir yazılım çözümüdür.

### Vizyonumuz
Afet sonrası hızlı ve doğru karar alma süreçlerini desteklemek adına;
- **Koordinasyon:** Ekiplerin planlı ilerlemesini sağlamak.
- **Hız:** Enkaz tespiti ve bölge analizini yapay zeka ile otomatikleştirmek.
- **Şeffaflık:** İşlenen verileri etkileşimli haritalar üzerinden sahadaki ekiplere sunmak.

### Görüntü İşleme Modeli
- **Enkaz Tespiti:** Kendi oluşturduğumuz 41 bin fotoğraflı özgün datasetimiz ile yolov8m modelini eğittik ortaya çıkan modeli enkaz tespitinde kullandık
- **Akıllı Haritalama:** Rasperry pi ile çektiğimiz fotoğrafların koordinat verilerine dayalı, birleştirilmiş mozaik harita katmanları.
- **Arayüz:** Streamlit tabanlı interaktif kontrol paneli ve geliştireceğimiz mobil intrnetsiz uygulamamız.
- **Veri Analitiği:** Tespit edilen enkazların anlık istatistiksel raporlanması, afet ekiplerine sunulması

---
*Projemizin detaylarını incelemek isterseniz aşağıdaki adımları inceleyebilirsiniz.*

### Yazılımı Nasıl Çalıştırırım?
1. Bizle İletişime geçerek model dosyalarını talep edebilirsiniz demo için sonraki adımları takip edin
2. [Afet_Analiz_Sistemi.py dosyasını bulun](https://github.com/amanitav/GTLRescuerSoftware/blob/main/Afet_Analiz_Sistemi.py) bu linke girin ve IDE'n kodları kopyalayın.
3. Gerekli kütüphaneleri yükleyin: `pip install ultralytics streamlit folium streamlit-folium opencv-python`
4. Terminale şu komutu girin: `streamlit run "dosya adınız".py`
Not (Önemli): kodunuzu çalıştırdığınızda bize ulaşmadan sadece uydu görüntüleri kısmını çalıştırabileceksiniz harici işlevlerde hata verecektir. Kullanılan fotoğraflar ve eğittiğmiz yolo modeli sizde bulunmaması bu hatanın kaynağıdır. An itibariyle TEKNOFEST LİSELERARSI İHA Yarışmasında olduğumuzdan ötürü Modeli sizlerle paylaşamayız telafi olarak size diğer afet haritası ve işlenmiş harita sekmelerinin fotoğrafını yükledik.

#### Proje Ekran Görüntüleri
**Afet Haritası:**
([Afet Haritası](https://github.com/amanitav/GTLRescuerSoftware/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-03-16%20180119.png))

**İşlenmiş Harita (Enkaz Tespiti):**
([İşlenmiş Harita](https://github.com/amanitav/GTLRescuerSoftware/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-03-16%20180137.png))



### Geliştirme Süreci Hakkında Bilgilendirme
Projemiz aktif bir geliştirme sürecindedir. Şu an GitHub üzerinden paylaşılan model, 20 epochluk bir eğitim aşamasından elde edilen öncelikli prototip verileridir. Ekibimiz, enkaz tespitindeki doğruluk payını maksimize etmek adına eğitim ve optimizasyon çalışmalarına devam etmektedir.

## HÜMATasarım : Özgün VTOL İHA ve Yer İstasyonu Tasarımı

### Vizyonumuz 
-**Verimlilik:** 4+1 Twinboom VTOL Konfigürasyon iniş/kalkış alanının kısıtlı olduğu afet şartlarında verimlilik ve stabilite sağlar
-**Modülerlik ve Taşınabilirlik:** Kanatların ve Kuyruğun Gövdeden Ayrılabildiği Konfigürasyon İHA'nın 118x100x50 cm lik bir kutuda taşınabilmesine olanak sağlar
-**Güvenilirlik:** Yedekli Sistem Mimarisi ve Kullanılan Kompozit ve Kaliteli Malzemeler Görev Güvenliğini Sağlar
### İHA Teknik Çizimi
<img width="6250" height="4419" alt="Elektronik (6)" src="https://github.com/user-attachments/assets/56b9e826-30ca-4e10-ac04-48bc7a81280c" />

### Anisopetra ile Biyomimikri

<img width="6250" height="4419" alt="Elektronik (7)" src="https://github.com/user-attachments/assets/926f3962-0445-488a-9b5f-debe2f4c19a4" />

### Taşıma Çantası ve İHA'nın Modüler Tasarımı

<img width="6250" height="4419" alt="Elektronik (8)" src="https://github.com/user-attachments/assets/c96ee556-90fb-4056-a065-d3290f1dcccb" />

### Yer İstasyonu Taşıma Çantası

<img width="6250" height="4419" alt="Elektronik (9)" src="https://github.com/user-attachments/assets/79775f5a-7921-425a-9d95-28c95a238122" />

## HÜMADonanım : Donanım Şemamız ->
 
<img width="4419" height="6250" alt="Elektronik (2)" src="https://github.com/user-attachments/assets/81dcc3d5-cac9-487e-ac7c-c11776603149" />

## Ar-Ge ve İLETİŞİM
Projemiz Aktif geliştirme aşamasındadır ve sizlerden gelecek geri dönüşler bizim için çok kıymetli. Maddi/Teknik açıdan destek sağlamak isterseniz bize ulaşabilirsiniz
İLETİŞİM: gokturkslegacy@gmail.com

İLGİNİZ İÇİN TEŞEKKÜRLER
