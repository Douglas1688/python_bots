from bs4 import BeautifulSoup
import pandas as pd
import requests
import time as tiempo
import datetime


def scrap_universo():  
    lst=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    today = datetime.datetime.today()

    d = '{:%d}'.format(today)
    m  = lst[int('{:%m}'.format(today))-1]
    y = '{:%Y}'.format(today)
    
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    chat_id="1053185415"
    #chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    
  
    url =f'https://www.eluniverso.com/clasificados/empleos/buscar?termino=&categoria=128562&fecha%5Bvalue%5D%5Bdate%5D={d}+{m}+{y}'

    headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
    
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'lxml')


    titulo = list()
    localidad = list()
    contenido = list()
    fecha = list()


    for i in soup.find_all('span',class_='titulo-clasificado'):
        titulo.append(i.text.upper())
    longitud = len(titulo)
    for i in range(longitud):
        localidad.append('GUAYAQUIL')
    for i in soup.find_all('div',class_='field-content'):
        contenido.append(i.text.replace('#','nº'))        


    for i in soup.find_all('span',class_='fecha-clasificado'):
        fecha.append(i.text)
           
    
    longitud = len(titulo)
        
    df = pd.DataFrame({'Nombre':titulo,'Contenido':contenido,'Localidad':localidad,'Fecha':fecha},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]  

    for elem in df.index:
        requests.post(url_req+"{}\nDescripción:  {}\n{}{}\nFECHA:  {}\n".format(df['Nombre'][elem],
            str(df['Contenido'][elem]),chr(128205),df['Localidad'][elem],df['Fecha'][elem]))
        tiempo.sleep(5)




scrap_universo()