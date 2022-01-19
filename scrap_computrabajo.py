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
    # api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    #api_tiny = "https://tinyurl.com/api-create.php?url="
    token="1463804463:AAFiAwYmUSo4qEXF1tVTQp1WseuEyHU0npI"
    # chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    #s = pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')
    jobs = list()
    address = list()
    links = list()

    for it in range(1,4):    
        url = "https://www.computrabajo.com.ec/ofertas-de-trabajo/?by=publicationtime&p={}".format(it)
        
        browser = start_chrome(url,headless=True)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        # for x in soup.find_all('a',class_='js-o-link'):
        #     jobs.append(x.text.upper())
        for elem in soup.find_all('article',class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m'):
            for i in elem.find_all('a',class_='js-o-link fc_base'):
                jobs.append(i.text)
        for elem in soup.find_all('article',class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m'):
            for i in elem.find_all('p',class_='fs16 fc_base mt5 mb10'):
                address.append(i.text)
        for elem in soup.find_all('article',class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m'):
            for i in elem.find_all('a',class_='js-o-link fc_base'):
                links.append('https://www.computrabajo.com.ec'+i['href'])
        
        
    df = pd.DataFrame({'Fuente':'CompuTrabajos','Nombre':jobs,'Localidad':address,'Links':links},index=list(range(1,(len(jobs)+1))))
    df = df.iloc[::-1]
    for elem in df.index:
        requests.post(url_req+"Fuente: {}\nPuesto: {}\nLocalidad:  {}\nLINK DE POSTULACIÓN:\n{}.".format(df['Fuente'][elem],df['Nombre'][elem], df['Localidad'][elem],df['Links'][elem]))
        tiempo.sleep(5)
        
scrapp_compu()
