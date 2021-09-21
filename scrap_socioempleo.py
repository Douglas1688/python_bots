import time as tiempo
from requests.api import request
import telepot
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrap_socio():
    token="1463804463:AAHYnABJQgZmE1seZ8xe0xH5HH7HnL-OxV8"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    # url = "https://socioempleo.trabajo.gob.ec/socioEmpleo-war/paginas/ofertas/verOferta.jsf?idOfeLab=257100"
    # page = requests.get(url)
    # soup = BeautifulSoup(page.content,'html.parser')
    # print(soup.find_all('div',id='content'))
    # for elem in soup.find_all('div', id='content'):
    #     for x in elem.find_all(class_='ui-panelgrid-cell form-input'):
    #         print(x.text)
    # for i in range(257100,257200):
    #     requests.post(url_req+"https://socioempleo.trabajo.gob.ec/socioEmpleo-war/paginas/ofertas/verOferta.jsf?idOfeLab="+f"{i}")
    #     tiempo.sleep(5)
    url = "https://socioempleo.trabajo.gob.ec/socioEmpleo-war/paginas/ofertas/verOferta.jsf?idOfeLab="
    desde = int(input("Desde:"))
    hasta = int(input("Hasta:"))
    for i in range(desde,hasta):
        if requests.get(url+f"{i}", verify=False).status_code == 200:
            requests.post(url_req+url+f"{i}")
            tiempo.sleep(5)

scrap_socio()
