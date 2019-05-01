# PTT圖片下載器 (Python) For Windows and Linux

A crawler picture for web PTT

* [Demo Video NEW](https://youtu.be/iAkdZP_Tcyo)  - Windows - 2017/4/23 update
* [Demo Video](https://www.youtube.com/watch?v=YIFTQnE2wuk)  - Linux
* [Demo Video](https://www.youtube.com/watch?v=aA4EDhxNRYo)  - Windows

## 教學

請先確認電腦有安裝 [Python 3.6.2](https://www.python.org/)

接著安裝套件

請先切換到該目錄底下，接著在你的命令提示字元 (cmd ) 底下輸入

>pip install -r requirements.txt

基本上安裝應該沒什麼問題。

![alt tag](http://i.imgur.com/2VUMQ0R.jpg)

## 特色

* 抓取PTT 圖檔(包含推文)
* 可指定要抓取的看板以及推文數多少以上

## 輸出格式

* 資料夾為文章標題加上推文數，資料夾內為圖片

## 效能優化

在 python 中有 [Multiprocessing](https://docs.python.org/3.6/library/multiprocessing.html) 以及 [Threading](https://docs.python.org/3/library/threading.html)，兩個使用的時機用比較容易的區分分法為，

當有高 CPU ( CPU-bound ) 計算的工作時，我們使用 [Multiprocessing](https://docs.python.org/3.6/library/multiprocessing.html)

當有大量 I/O ( I/O-bound ) 的工作時，我們使用 [Threading](https://docs.python.org/3/library/threading.html)

****使用 [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) 優化效能****

本範例來說，我們大量下載圖片，是使用 [Threading](https://docs.python.org/3/library/threading.html) 才對，不過我們之前使用 [Multiprocessing](https://docs.python.org/3.6/library/multiprocessing.html) 。

當下載量大時，速度會差到兩倍 , 在這種 大量 I/O ( I/O-bound ) 的情境下 ，使用 [Threading](https://docs.python.org/3/library/threading.html) 才是對的選擇。

建議使用 python 3.5 以上，因為 max_workers 如果沒有特別指定，預設會使用 CPU*5 的 workers 數量，如下說明

```pyhon
concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='')
```

參考連結 [https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)

## 使用方法

* 方法一(指定看板抓圖)

```cmd
python beauty_spider2.py [板名] [爬蟲起始的頁面] [爬幾頁] [推文多少以上]
```

* 方法二(指定網址抓圖)

```cnd
python download_beauty.py [輸入內容.txt]
```

如果要從最新頁面開始爬 第一個參數請填 -1

爬蟲是利用 PTT 網頁版，所以頁面以網頁版為標準。

請參考：

```url
https://www.ptt.cc/bbs/AKB48/index.html
```

## 執行範例

* 範例一(指定看板抓圖)

```cmd
python beauty_spider2.py beauty -1 3 10
```

爬PTT beauty板(表特板) 3頁 文章內容，然後只下載 推文數>=10 的文章內容圖片

### 執行畫面 - 1

![alt tag](http://i.imgur.com/EclywBO.jpg)

### 輸出畫面 - 1

![alt tag](http://i.imgur.com/CmcheN3.jpg)
![alt tag](http://i.imgur.com/C1E30JX.jpg)

也可以指定其他看板，如下

```cmd
python beauty_spider2.py AKB48 -1 3 10
```

* 範例二(指定網址抓圖)

```cmd
python download_beauty.py input.txt
```

爬 input.txt 檔案內的PTT文章連結圖片 , input.txt 檔案

![alt tag](http://i.imgur.com/dtcfWUy.jpg)

### 執行畫面 - 2

![alt tag](http://i.imgur.com/fmu5c8v.jpg)

### 輸出畫面 - 2

![alt tag](http://i.imgur.com/gtdPFCE.jpg)
![alt tag](http://i.imgur.com/hw9a8j0.jpg)
![alt tag](http://i.imgur.com/lPKRJnJ.jpg)

## 執行環境

* Python 3.6.2

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
