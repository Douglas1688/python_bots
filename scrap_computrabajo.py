import sys 
import time as tiempo
import telepot 
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pyshorteners
from helium import start_chrome

def scrapp_compu():
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    #api_tiny = "https://tinyurl.com/api-create.php?url="
    token="1463804463:AAGhxDuKJCNDd7R_fDawFXRmGXvJ9uPyKNo"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    #s = pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')
    jobs = list()
    address = list()
    company= list()
    #time = list()
    links = list()
    links_aux = list()
    for it in range(1,4):    
        url = "https://www.computrabajo.com.ec/ofertas-de-trabajo/?by=publicationtime&p={}".format(it)
        
        browser = start_chrome(url,headless=True)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for x in soup.find_all('a',class_='js-o-link'):
            jobs.append(x.text.upper())
        for x in soup.find_all('span',itemprop='addressLocality'):
            address.append(x.text)

        for x in soup.find_all('span',itemprop='name'):
            company.append(x.text)
        for x in soup.find_all('a',class_='js-o-link'):
            links_aux.append('https://www.computrabajo.com.ec'+x['href'])


        
    
    # for elem in links_aux:
    #     response = requests.get(api_adfocus+elem)
    #     b = response.content
    #     links.append(b.decode('utf-8'))

    longitud = len(jobs)
    df = pd.DataFrame({'Fuente':'Computrabajos','Nombre':jobs,'Localidad':address,'Empresa':company,'Links':links_aux},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]
    for elem in df.index:
        requests.post(url_req+"{}\n{}\n{}{}\nEmpresa:  {}\nLINK DE POSTULACIÓN:\n{}.".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
        df['Localidad'][elem],df['Empresa'][elem],df['Links'][elem]))
        tiempo.sleep(5)
        
scrapp_compu()
