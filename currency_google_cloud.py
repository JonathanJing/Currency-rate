import re
import time
import json
import urllib.request as ur
from datetime import datetime
from bs4 import BeautifulSoup

#Time
i = 0.1

#Get USD-CNY currency
url_USD_CNY = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNY&apikey=6D37A0038RJFIWBK'
html_USD_CNY = ur.urlopen(url_USD_CNY).read().decode()
info_USD_CNY = json.loads(html_USD_CNY)
er_USD_CNY = float(info_USD_CNY['Realtime Currency Exchange Rate']['5. Exchange Rate'])

#Get USD-CNH currency, CNH for "Chinese Yuan Offshore"
time.sleep(i)
url_USD_CNH = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNH&apikey=6D37A0038RJFIWBK'
html_USD_CNH = ur.urlopen(url_USD_CNH).read().decode()
info_USD_CNH = json.loads(html_USD_CNH)
er_USD_CNH = float(info_USD_CNH['Realtime Currency Exchange Rate']['5. Exchange Rate'])

#Get BTC-CNY currency
time.sleep(i)
url_BTC_CNY = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=6D37A0038RJFIWBK'
html_BTC_CNY = ur.urlopen(url_BTC_CNY).read().decode()
info_BTC_CNY = json.loads(html_BTC_CNY)
er_BTC_CNY = float(info_BTC_CNY['Realtime Currency Exchange Rate']['5. Exchange Rate'])

#Get BTC-USD currency
time.sleep(i)
url_BTC_USD = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=6D37A0038RJFIWBK'
html_BTC_USD = ur.urlopen(url_BTC_USD).read().decode()
info_BTC_USD = json.loads(html_BTC_USD)
er_BTC_USD = float(info_BTC_USD['Realtime Currency Exchange Rate']['5. Exchange Rate'])

#Caculate currenct USD-CNY in BTC
er_BTC_CNY_USD = er_BTC_CNY/er_BTC_USD

#get USD-CNY from BOC
time.sleep(i)
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'http://www.boc.cn/sourcedb/whpj'
headers={'User-Agent':user_agent,}

request = ur.Request(url,None,headers)
response = ur.urlopen(request)
html = response.read()

soup = BeautifulSoup(html, "html.parser")
tags = soup('td')

d_en = 0
for tag in tags:
    name = tag.get_text()
    if name == "美元":
      d_en = 8
    if d_en > 0:
      d_en -= 1
    if d_en is 4:
      name = float(name)
      #name = name/100
      print("中行现汇卖出价:", round(name/100,2))

print('在岸人民币汇率:', round(er_USD_CNY,2))
print('离岸人民币汇率:', round(er_USD_CNH,2))
print('比特币人民币汇率:',round(er_BTC_CNY_USD,2))
print('\n')
print('比特币-人民币汇率:', round(er_BTC_CNY,2))
print('比特币-美元汇率:', round(er_BTC_USD,2))
