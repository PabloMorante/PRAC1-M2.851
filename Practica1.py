#!/usr/bin/env python
# coding: utf-8

# In[21]:



#Práctica1 Web Scraping

import requests 
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import csv
from datetime import datetime

#Importo la url 
url = 'https://coinmarketcap.com/all/views/all/'
page = requests.get(url)
tiempo= datetime.now().strftime("%d-%m-%Y %H:%M")
soup = BeautifulSoup(page.content,'html.parser')


#Despues de ver como son los datos, vemos que son formato Json
name = soup.find('script', id="__NEXT_DATA__", type='application/json')
data_cry=json.loads(name.contents[0])
bucle_n= data_cry['props']['initialState']['cryptocurrency']['listingLatest']['data']


#Hacemos un bucle para obtener los datos y unirlos
tabla_cr=[]
for i in bucle_n: 
    
    Nombre=i['name']
    Simbolo=i['symbol']
    precio= i['quotes'][0]['price']
    Cap_mercado= i['quotes'][0]['marketCap']
    Circ_supply=i['circulatingSupply']
    Volumen_24h=i['quotes'][0]['volume24h']
    Porcent_1h=i['quotes'][0]['percentChange1h']
    Porcent_24h=i['quotes'][0]['percentChange24h']
    Porcent_7d=i['quotes'][0]['percentChange7d']
    Porcent_30d=i['quotes'][0]['percentChange30d']
    Porcent_YTD=i['quotes'][0]['ytdPriceChangePercentage']
    Fecha_ext= tiempo
    tabla_cr.append((Nombre,Simbolo,precio,Circ_supply,Cap_mercado,Volumen_24h,Porcent_1h,Porcent_24h,Porcent_7d,Porcent_30d,Porcent_YTD, Fecha_ext))

tabla_final= pd.DataFrame(tabla_cr, columns=['Nombre','Simbolo','Precio','Supply en circulacion','Marketcap','Volumen 24h','%1h','%24h','%7 días','%1 mes','% YTD', 'Fecha extracción'])


campos=['Nombre','Simbolo','Precio','Supply en circulacion','Marketcap','Volumen 24h','%1h','%24h','%7 días','%1 mes','% YTD', 'Fecha extracción']

tabla_final


with open('C:\\Users\\Pablo\\dataset.csv', 'w', newline="") as csvFile: 

    
    writter=csv.DictWriter(csvFile, fieldnames=campos)
    writter.writeheader()

    writer= csv.writer(csvFile)
    writer.writerows(tabla_cr)
    

