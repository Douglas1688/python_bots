import requests
from bs4 import BeautifulSoup
import pandas as pd
import time as tiempo

def scrap_ejob():
    token="1463804463:AAFiAwYmUSo4qEXF1tVTQp1WseuEyHU0npI"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_bxc = "https://bc.vc/api.php?key=e60a22c77869be83f8df5d556a50d1dd&uid=388979&url="
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="   
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
   
    title = list()
    links_aux = list()
    links = list()
    links_listos = list()
    locations = list()
    cities =['Guayaquil','Quito','Cuenca','Santo Domingo','Machala','Durán','Manta','Portoviejo','Loja','Ambato','Esmeraldas','Quevedo','Riobamba',
    'Milagro','Ibarra','Latacunga','Salinas','Azogues']

    for city in cities:
        i=0
        url= f'https://e-talent.jobs/bolsa-de-trabajo/?search_keywords=&search_location={city}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        for x in soup.find_all('div',class_='listing-title'):
            for y in x.find_all('h4'):
                title.append(y.text)
                i+=1
        for _ in range(i):
            locations.append(city.upper())

        for elem in soup.find_all("li"):
            for x in elem.find_all("a"):
                links_aux.append(x['href'])
                      

    links =[elem for elem in links_aux if '/trabajo' in elem]

    # for elem in links:
        # response = requests.get(api_adfocus+elem)
        # b = response.content
        # links_listos.append(b.decode('utf-8'))
        # tiempo.sleep(1)

    longitud = len(title)
   
    df = pd.DataFrame({'Fuente':'e-talent.jobs','Nombre':title,'Localidad':locations,'Link':links},index=list(range(1,(longitud+1))))
    for elem in df.index:
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
       df['Localidad'][elem],df['Link'][elem]))
        tiempo.sleep(5)



scrap_ejob()
