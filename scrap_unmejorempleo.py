from bs4 import BeautifulSoup
import requests
import pandas as pd
import time as tiempo
import pyshorteners

def scrap_unmejorempleo():
    token="1463804463:AAGhxDuKJCNDd7R_fDawFXRmGXvJ9uPyKNo"
    chat_id="-1001458610971"
    #chat_id="1053185415"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    
    jobs = list()
    address = list()
    links = list()
    links_aux= list()
    url = 'https://www.unmejorempleo.com.ec/busqueda_resultados.php?f=1'

    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    i = soup.find_all(class_='no-margin-top')
 
    l = soup.find_all(class_='text-primary')


    for elem in i:jobs.append(elem.text.strip().upper())

    for elem in l: address.append(elem.text.strip().upper())

    for p in soup.find_all(class_='no-margin-top'):
        for track in p.find_all('a'):
            links_aux.append('https://www.unmejorempleo.com.ec/'+track['href'])

    """for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))"""


    longitud = len(jobs)

    df = pd.DataFrame({'Fuente':'Un mejor Empleo','Nombre':jobs,'Localidad':address,'Links':links_aux,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]
        

    for elem in df.index:    
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}\nNOTA: {}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
        df['Localidad'][elem],df['Links'][elem],df['Nota'][elem]))
        tiempo.sleep(5)
    

scrap_unmejorempleo()
    
