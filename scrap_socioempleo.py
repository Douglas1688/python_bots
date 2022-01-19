import time
from requests.api import request
import telepot
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def scrap_socio():
    token="1463804463:AAFiAwYmUSo4qEXF1tVTQp1WseuEyHU0npI"
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    chat_id="-1001458610971"
    # chat_id="1053185415"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    url_base = "https://encuentraempleo.trabajo.gob.ec/socioEmpleo-war/paginas/ofertas/verOferta.jsf?idOfeLab="
    desde = int(input("Desde: "))
    hasta = int(input("Hasta: "))
    lista = []
    try:
        for i in range(desde,hasta+1):        
            url = url_base+f"{i}"
            page = requests.get(url)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text,'html.parser')
                # print(soup)
                table = soup.find_all("table")[3]
                i = 0
                # th = table.find_all()
                for elem in table.find_all('td', class_='ui-panelgrid-cell form-input')[:8]:
                    if i == 1 or i == 4:
                        pass
                    else:
                        lista.append(elem.text)
                    i += 1
                lista.append(url)
                requests.post(url_req+f"Fuente: Encuentra Empleo\nPuesto: {lista[0]}\nCiudad: {lista[1]}\nParroquia: {lista[2]}\nFecha de Publicación: {lista[4]}\nFecha de Finalización: {lista[5]}\nLink: {lista[6]}")
                lista.clear()
                time.sleep(5)
    except Exception as e:
        print(e)
    

scrap_socio()
