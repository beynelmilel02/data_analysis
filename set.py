import pandas as pd 

df=pd.read_csv('14.BTC_USDC_Dataset.csv',low_memory=False)
df['date'] = pd.to_datetime(df['date'])

# veriler düzensiz sırala 
df = df.sort_values(by='date')

# indexi sildim index yeni sütün oluşturuyordu ilk sütün index olmalı model için
df.to_csv('duzeltilmis_btc.csv', index=False)
