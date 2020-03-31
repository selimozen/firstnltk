import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np



r = requests.get("https://www.n11.com/cok-satanlar")

soup = BeautifulSoup(r.content, "lxml")


urunler = soup.find_all("h3", attrs = {"class" : "productName"})
urunler1 = []
for urun in urunler:
    urunler1.append(urun.text)
    df = pd.DataFrame(urunler1, columns = ['Ürünler'])
    


satıcılar = soup.find_all("span", attrs = {"class" : "sallerName"})
satıcılar1 = []
for satıcı in satıcılar:
    satıcılar1.append(satıcı.text)
    df1 = pd.DataFrame(satıcılar1, columns = ['Satıcılar'])


yeni_fiyatlar = soup.find_all("a", attrs = {"class" : "newPrice"})
yeni_fiyatlar1 = []
for yeni_fiyat in yeni_fiyatlar:
    yeni_fiyatlar1.append(yeni_fiyat.text)
    df2 = pd.DataFrame(yeni_fiyatlar1, columns = ['Yeni_Fiyatlar'])


yapılan_oylamalar = soup.find_all("div", attrs = {"class" : "ratingCont"})
yapılan_oylamalar1 = []
for yapılan_oylama in yapılan_oylamalar:
    yapılan_oylamalar1.append(yapılan_oylama.text)
    df3 = pd.DataFrame(yapılan_oylamalar1, columns = ['Yapılan Oylamalar'])
    
new_data = pd.concat([df, df1, df2, df3], axis = 1)

new_data.to_csv("/home/mustafa/n11data.csv", index = False, header = True)
