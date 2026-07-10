import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv('set2.csv')

# 2. Sütun isimlerini Prophet'in istediği formata getir  ds ve y
df = df.rename(columns={'date': 'ds', 'close': 'y'})  #gerekli 2 sütün var ve sonucunda çıktıda 4 sütün verir prophet 


df['ds'] = pd.to_datetime(df['ds']) # Önce datetime yap
df['ds'] = df['ds'].dt.tz_localize(None) # Zaman dilimini sil

# BTC 7/24 açık olduğu için günlük ve haftalık mevsimselliği açtık ( farklı şekilde denenbilir)
model = Prophet(
    changepoint_prior_scale=0.05, # trend bias ayarı:::düşük değerler daha stabil ve yüksek fiyat toleransı demek 
    daily_seasonality=True, 
    weekly_seasonality=True,
    yearly_seasonality=True
)

# Modeli eğit 
model.fit(df)

# Gelecek için zaman tablosu (240 saat = 10 gün)    
future = model.make_future_dataframe(periods=240, freq='h') #period freq türünde mikttarı // frequeny olarak saatlikten devam ediyoruz 

# Tahmin yap
forecast = model.predict(future)

# plot oluşturma geçmiş ve gelecek tahminler ama sadece gelecek için olarak güncellenebilir 
fig1 = model.plot(forecast)
plt.title("BTC Saatlik Tahmin")
plt.show()

# Trend ve mevsimsellik bileşenlerini gör (Günlük, haftalık döngüler) gereksiz özellik silinebilir 
fig2 = model.plot_components(forecast)
plt.show()

### 10 günlük tahmin sonuçlarını yazdır  buradaki sütün isimleri prophet formatında 
tahmin_sonuclari = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(240)  

# Sütun isimlerini daha anlaşılır yapalım
tahmin_sonuclari.columns = ['Tarih', 'Tahmin_Fiyat', 'Min_Beklenti', 'Max_Beklenti']

print("GELECEK 24 BİRİMLİK BTC TAHMİNLERİ")
print(tahmin_sonuclari)

#kaydet yeni dosyaya
tahmin_sonuclari.to_csv('btc_gelecek_tahminleri.csv', index=False)
