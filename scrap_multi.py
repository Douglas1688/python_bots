"""from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.multitrabajos.com/empleos.html?recientes=true'

r = session.get(url)
r.html.render(sleep=1,keep_page=True,scrolldown=1)
page = r.html.find('h3')
for item in page:
    print(item.text)"""
import time as tiempo
from helium import start_chrome
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pyshorteners


def scrap_multitrabajo():
    
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    token="1463804463:AAGhxDuKJCNDd7R_fDawFXRmGXvJ9uPyKNo"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    #s=pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')

    title = list()
    location = list()
    links = list()
    links_aux=list()
    url = 'https://www.multitrabajos.com/empleos-publicacion-hoy.html'

    browser = start_chrome(url,headless=True)

    soup = BeautifulSoup(browser.page_source,'html.parser')
    t = soup.find_all('h2')
    l = soup.find_all('h3', class_="Card__Location-i6v2cb-9 dRXvyB")

    for elem in t:title.append(elem.text.upper())
    for elem in l:location.append(elem.text.upper())

    for elem in soup.find_all('a',class_='Card__CardContentWrapper-i6v2cb-1 cdmEkq'):
        links_aux.append('https://www.multitrabajos.com'+elem['href'])

    """for elem in links_aux:
            response = requests.get(api_adfocus+elem)
            b = response.content
            links.append(b.decode('utf-8'))"""
 

    longitud = len(title)
    df = pd.DataFrame({'Fuente':'Multitrabajos','Nombre':title,'Localidad':location,'Link':links_aux,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))

    for elem in df.index:
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}\n{}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
            df['Localidad'][elem],df['Link'][elem],df['Nota'][elem]))
        tiempo.sleep(5)

scrap_multitrabajo()
