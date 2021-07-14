import time as tiempo
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


def scrapp_compu():
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    
    jobs = list()
    address = list()
    company= list()
    time = list()
    links = list()
    links_aux = list()
    for it in range(1,4):    
        url = "https://www.computrabajo.com.ec/ofertas-de-trabajo/?by=datelastup&p={}".format(it)
        
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')

        j = soup.find_all('a',class_='js-o-link')
        a = soup.find_all('span',itemprop='addressLocality')    
        c = soup.find_all('span',itemprop='name')
        h = soup.find_all('span',class_='dO')        

        for p in soup.find_all(id='p_ofertas'):
            for track in p.find_all('a',class_='js-o-link'):
                links.append('https://www.computrabajo.com.ec'+track['href'])       

        for i in j:jobs.append(i.text.strip().upper())
        for x in a:address.append(x.text.strip().upper())
        for z in c:company.append(z.text.strip())
        for a in h:time.append(a.text.strip())      


    """for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))"""  

    longitud = len(jobs)
    df = pd.DataFrame({'Fuente':'Computrabajos','Nombre':jobs,'Localidad':address,'Empresa':company,'Hora':time,'Links':links,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]
    for elem in df.index:
        requests.post(url_req+"{}\n{}\n{}{}\nEmpresa:  {}\nFecha:  {}\nLINK DE POSTULACIÓN:\n{}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
        df['Localidad'][elem],df['Empresa'][elem],df['Hora'][elem],df['Links'][elem]))
        tiempo.sleep(5)


