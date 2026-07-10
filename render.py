import streamlit as st  
#from mdl import fig1
import pandas as pd 
import matplotlib.pyplot as plt
import requests
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=30 * 1000, key="fiyat_guncelle")

def btc_canli_fiyat():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        data = requests.get(url).json()
        return float(data['price'])
    except:
        return None
    


df = pd.read_csv('btc_gelecek_tahminleri.csv')  
df['Tarih'] = pd.to_datetime(df['Tarih'])

fig,ax=plt.subplots(figsize=(15, 7))
ax.plot(df['Tarih'],df['Tahmin_Fiyat'])

ax.set_title('BTC Fiyat Tahmini (Gelecek 10 Gün)')
ax.set_xlabel('Tarih')
ax.set_ylabel('Tahmin Edilen Fiyat (USD)')
ax.grid(True)
st.set_page_config(layout="wide")
st.title(":yellow[BTC Fiyat Tahmini] 🪙")

st.write("btc prediction for next 10 days ")
c1 ,c2=st.columns(2)
with c1:
    st.pyplot(fig)
with c2:
    st.dataframe(df)

su_anki_fiyat = btc_canli_fiyat()

st.sidebar.metric(
        label="Canlı BTC/USDT (Binance)", 
        value=f"${su_anki_fiyat:,.2f}",
        delta="Canlı Veri"
        
    )

