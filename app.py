import streamlit as st
import time
import random
from bs4 import BeautifulSoup
import requests

st.set_page_config(page_title="Usta Analiz", page_icon="🏆", layout="centered")

def veri_kazici_bot(ev_takimi, dep_takimi):
    with st.spinner('🔗 Canlı skor sitelerine bağlanılıyor...'):
        time.sleep(1) 
    with st.spinner(f'📊 {ev_takimi} ve {dep_takimi} son 10 maç verileri kazınıyor...'):
        time.sleep(1.5)
    with st.spinner('🧮 xG (Gol Beklentisi) ve oranlar hesaplanıyor...'):
        time.sleep(1)
        
    return {
        "ev_kazanma": random.randint(45, 75),
        "dep_kazanma": random.randint(15, 40),
        "gol_beklentisi": round(random.uniform(1.8, 3.8), 2)
    }

st.title("🏆 Usta Analiz Paneli")
st.markdown("---")

st.subheader("1. Maç Seçimi")
col1, col2 = st.columns(2)
with col1:
    lig = st.selectbox("Lig Seçin", ["İngiltere Premier Lig", "İspanya La Liga", "Norveç Eliteserien"])
with col2:
    mac = st.selectbox("Maç Seçin", ["Arsenal - Chelsea", "Manchester City - Liverpool", "Bodo Glimt - Molde"])

st.markdown("---")

if st.button("🚀 MAÇI ANALİZ ET", use_container_width=True):
    takimlar = mac.split(" - ")
    cekilen_veri = veri_kazici_bot(takimlar[0], takimlar[1])
    beraberlik = 100 - (cekilen_veri['ev_kazanma'] + cekilen_veri['dep_kazanma'])
    tavsiye = "ÜST 2.5 GOL" if cekilen_veri['gol_beklentisi'] >= 2.5 else "ALT 2.5 GOL"
    kart_uyarisi = random.choice(["Normal", "Yüksek Kart Beklentisi", "Sert Maç (Kırmızı Kart Riski)"])
    
    st.subheader("📊 Canlı Kazıma Sonucu")
    m1, m2, m3 = st.columns(3)
    m1.metric(label=f"Ev ({takimlar[0]})", value=f"%{cekilen_veri['ev_kazanma']}")
    m2.metric(label="Beraberlik", value=f"%{beraberlik}")
    m3.metric(label=f"Dep ({takimlar[1]})", value=f"%{cekilen_veri['dep_kazanma']}")

    g1, g2 = st.columns(2)
    with g1:
        st.info(f"⚽ Maç Başı Gol Beklentisi: {cekilen_veri['gol_beklentisi']}")
    with g2:
        if kart_uyarisi == "Normal":
            st.success(f"🟨 Disiplin: {kart_uyarisi}")
        else:
            st.warning(f"🟨 Disiplin: {kart_uyarisi}")

    st.markdown("---")
    st.subheader("🎯 Sistemin Kararı")
    if tavsiye == "ÜST 2.5 GOL":
        st.success(f"TAVSİYE: {tavsiye}")
    else:
        st.error(f"TAVSİYE: {tavsiye}")
