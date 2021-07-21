import time as tiempo
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import pyshorteners
import os

def scrap_joraempleo():
    token="1463804463:AAGhxDuKJCNDd7R_fDawFXRmGXvJ9uPyKNo"
    chat_id="-1001458610971"
    #chat_id="1053185415"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    #s=pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')
    jobs = list()
    address = list()
    links = list()
    links_aux=list()
    for i in range(1,3):
        url = f'https://ec.jora.com/j?l=&p={i}&q=&since=lv&sp=recent_homepage&st=date&surl=0&tk=XSPdy1yZK16tDKJYL2HW-IXVwo91dxCbgmMurZwlN'
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        
        j = soup.find_all(class_='job-title')
        a= soup.find_all(class_='job-location')
        l = soup.find_all(class_='job-item')

        for elem in j:jobs.append(elem.text.strip().upper())
        for elem in a:address.append(elem.text.strip())
        for elem in l:links_aux.append('https://ec.jora.com'+elem['href'])

    for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))
   
    longitud = len(jobs)

    df = pd.DataFrame({'Fuente':'Jora Empleos','Nombre':jobs,'Localidad':address,'Links':links},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]        

    for elem in df.index:    
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
        df['Localidad'][elem],df['Links'][elem]))
        tiempo.sleep(5)
    
scrap_joraempleo()
