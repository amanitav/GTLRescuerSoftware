import cv2
import numpy as np
import folium
from folium.raster_layers import ImageOverlay
from ultralytics import YOLO
import streamlit as st
from streamlit_folium import st_folium

MERKEZ = [37.5714, 36.9335]

def birlestirilmis_harita_olustur():

    model = YOLO('runs/detect/bina_tespit_projesi/yolov8m_bina_egitimi_v17/weights/last.pt')

    sonuclar = [model.predict(source=foto, conf=conf)[0] for foto, conf in
                [("foto3.jpg", 0.5), ("foto1.jpg", 0.3), ("foto4.jpg", 0.5), ("foto2.jpg", 0.3)]]

    toplam_enkaz = sum([len(r.boxes) for r in sonuclar])

    islenmis_fotolar = [cv2.resize(r.plot(), (640, 640)) for r in sonuclar]
    birlesik = np.vstack((np.hstack((islenmis_fotolar[0], islenmis_fotolar[1])),
                          np.hstack((islenmis_fotolar[2], islenmis_fotolar[3]))))

    cv2.imwrite("birlesik_harita_islenmis.png", birlesik)

    m = folium.Map(location=MERKEZ, zoom_start=17, tiles=None)

    ImageOverlay(image="birlesik_harita_islenmis.png", bounds=[[37.5684, 36.9275], [37.5744, 36.9395]],
                 opacity=1.0).add_to(m)

    return m, toplam_enkaz

def afet_haritasini_olustur():

    m = folium.Map(location=MERKEZ, zoom_start=17, tiles=None)

    overlay_verileri = [
        {"isim": "foto1.jpg", "bounds": [[37.5714, 36.9335], [37.5744, 36.9395]]},
        {"isim": "foto2.jpg", "bounds": [[37.5684, 36.9335], [37.5714, 36.9395]]},
        {"isim": "foto3.jpg", "bounds": [[37.5714, 36.9275], [37.5744, 36.9335]]},
        {"isim": "foto4.jpg", "bounds": [[37.5684, 36.9275], [37.5714, 36.9335]]}
    ]

    for foto in overlay_verileri:
        ImageOverlay(image=foto["isim"], bounds=foto["bounds"], opacity=1.0).add_to(m)
    return m

def uydu_haritasini_olustur():

    m = folium.Map(location=MERKEZ, zoom_start=17)
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google',
        name='Uydu'
    ).add_to(m)
    return m

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Mod Seçim Paneli")
    secim = st.radio("Harita Seçin:", ["Afet Haritası", "Uydu Görüntüleri","İşlenmiş Harita"])

if secim == "Afet Haritası":
    st.subheader("Afet Bölgesi Analiz Haritası")
    m = afet_haritasini_olustur()
    st_folium(m, width=1300, height=750)

elif secim == "Uydu Görüntüleri":
    st.subheader("Uydu Görüntüsü")
    m = uydu_haritasini_olustur()
    st_folium(m, width=1300, height=750)
else:
    st.subheader("Görüntü İşlenmiş Harita")
    m, sayi = birlestirilmis_harita_olustur()
    st.metric(label="Toplam Tespit Edilen Enkaz Sayısı", value=sayi)
    st_folium(m, width=1300, height=750)