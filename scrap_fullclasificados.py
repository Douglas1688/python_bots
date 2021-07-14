import sys 
import time as tiempo
import telepot 
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrapp_fullclasificados():
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    #api_tiny = "https://tinyurl.com/api-create.php?url="
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    #s = pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')
    jobs = list()
    info = list()
    links = list()
    links_aux = list()

    for i in range(1,4):
       
        url = "https://www.fullclasificados.ec/empleos/avisos/solicitan/profesionales?max_per_page=10&order_search=date_desc&search_results_view=lineal&page={}".format(i)

        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')     
        for x in soup.find_all('article',class_='advice lineal'):
            for elem in x.find_all('div',class_='column2'):
                for y in elem.find_all('a'):
                    jobs.append(str(y.text).strip())



        for x in soup.find_all('article',class_='advice lineal'):
            for elem in x.find_all('div',class_='column2'):
                for y in elem.find_all('span',class_="resume-advice"):
                    info.append(str(y.text).strip())
                   


        for x in soup.find_all('article',class_='advice lineal'):
            for elem in x.find_all('div',class_='column2'):
                for y in elem.find_all('a'):
                    links_aux.append(y['href'])
        
    for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))

    longitud = len(jobs)
    df = pd.DataFrame({'Nombre':jobs,'Descripcion':info,'Links':links},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]
    for elem in df.index:
        requests.post(url_req+"Fuente: Full Clasificados\n{}\nDescripción: {}\nMás Información:\n{}\nNOTA: ESPERAR 6 SEGUNDOS, LUEGO PRESIONAR 'SKIP'.".format(df['Nombre'][elem],df['Descripcion'][elem],df['Links'][elem]))
        tiempo.sleep(5)




scrapp_fullclasificados()