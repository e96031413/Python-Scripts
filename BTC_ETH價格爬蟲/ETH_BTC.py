import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def coingecko_crawler(url):
    res=requests.get(url)
    prices=res.json()['stats']
    df=pd.DataFrame(prices)
    df.columns=['datetime', 'USD']
    df['datetime']=pd.to_datetime(df['datetime'], unit='ms')
    df['datetime'] += pd.DateOffset(hours=8)
    df.index=df['datetime']
    return df

def notify_image(msg, token, image):
    url='https://notify-api.line.me/api/notify'
    headers={'Authorization': 'Bearer ' + token}
    data={'message': msg}
    image=open(image, 'rb')
    imageFile={'imageFile': image}
    r=requests.post(url, headers=headers, data=data, files=imageFile)
    if r.status_code==requests.codes.ok:
        return '圖片發送成功！'
    else:
        return f'圖片發送失敗: {r.status_code}'

token='duWjLpIHAHm6bgb8AhKpqjIxePwcB62kboFSjPUuMtC'   
# 比特幣
url='https://www.coingecko.com/price_charts/1/usd/90_days.json'
btc=coingecko_crawler(url)
btc['100MA']=btc['USD'].rolling(window=100).mean()
btc[['USD', '100MA']].plot(kind='line')
last_time=str(btc.iloc[-1:].index.values[0])[0:19]
last_price=int(btc.iloc[-1:]["USD"].values[0])
plt.title(f'BTC {last_time} USD {last_price} ')
plt.xlabel('')
plt.ylabel('Price(USD)')
plt.grid(True)
plt.legend(['Price', '100 Hours AVG.'], loc='best') 
plt.savefig('btc_prices.jpg')
img=Image.open('btc_prices.jpg')       # 開啟檔案   
img=img.crop((18, 26, 590, 453))       # 裁切圖片去除外圍白邊  
img.save('btc_prices.jpg')                    # 回存檔案   
msg=f'\n比特幣 {last_time} 美金 {last_price} 元'
notify_image(msg, token, 'btc_prices.jpg')

# 乙太幣
url='https://www.coingecko.com/price_charts/279/usd/90_days.json'
eth=coingecko_crawler(url)
eth['100MA']=eth['USD'].rolling(window=100).mean()
eth[['USD', '100MA']].plot(kind='line')
last_time=str(eth.iloc[-1:].index.values[0])[0:19]
last_price=int(eth.iloc[-1:]["USD"].values[0])
plt.title(f'ETH {last_time} USD {last_price}')
plt.xlabel('')
plt.ylabel('Price(USD)')
plt.grid(True)
plt.legend(['Price', '100 Hours AVG.'], loc='best') 
plt.savefig('eth_prices.jpg')
img=Image.open('eth_prices.jpg')       # 開啟檔案   
img=img.crop((0, 26, 590, 453))       # 裁切圖片去除外圍白邊  
img.save('eth_prices.jpg')             # 回存檔案   
msg=f'\n乙太幣 {last_time} 美金 {last_price} 元'
notify_image(msg, token, 'eth_prices.jpg')
#plt.show()  # 測試時才使用