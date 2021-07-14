import time
from bs4 import BeautifulSoup
from helium import start_chrome
import requests
import os
import pandas as pd
import time as tiempo
import datetime
import pyshorteners


def scrap_hiring(archivo):

    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="  
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url=" 
    #s=pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')
    dir = 'C:/Users/GamaPrinter/PycharmProjects/python_bot/'
    #dir = 'C:/Users/Administrator/Desktop/'
    lst=[]
    with open(dir+archivo,'r') as f:
        for elem in f:
            lst.append(elem.replace('\n',''))
    title = list()
    company =list()
    links = list()
    links_aux = list()
    locations = list()

    for z in range(len(lst)):
        i=0
        url = 'https://'+lst[z]+'hiringroom.com/jobs'

        browser = start_chrome(url,headless=True)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for x in soup.find_all('div',class_='col-md-12'):
            for elem in x.find_all('h2'):
                title.append(elem.text.strip().upper())
                i+=1

        for x in soup.find_all('li',class_='vacantes'):
            for elem in x.find_all('a'):
                links_aux.append('https:'+elem['href'])

        for x in soup.find_all('li',class_='vacantes'):
            for elem in x.find_all('p',class_='location'):
                locations.append(elem.text.upper())
        for _ in range(i):
            company.append(lst[z].upper())
        #os.system('taskkill /f /im chrome.exe')
        

    
    """for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))"""



    longitud = len(title)   

    df = pd.DataFrame({'Nombre':title,'Empresa':company,'Localidad':locations,'Link':links_aux},index=list(range(1,(longitud+1))))
    for elem in df.index:
        requests.post(url_req+"{}\nEmpresa: {}\n{}{}\nLINK DE POSTULACIÓN:\n{}.".format(df['Nombre'][elem],df['Empresa'][elem],chr(128205),df['Localidad'][elem],df['Link'][elem]))
        tiempo.sleep(5)



scrap_hiring('hir4.txt')
