from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import datetime
def scrap_accion():


    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    chat_id="-1001458610971"
    #chat_id="1053185415"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="


    title = list()
    company = list()
    links = list()
    links_aux=list()
    loc = list()
    locations = list()
    for i in range(1,3):
        url = f"https://acciontrabajo.ec/buscar-empleos?o=d&p={i}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')

        
        for x in soup.find_all('article'):
            for elem in x.find_all('h2'):
                title.append(elem.text.strip().upper())
        for x in soup.find_all('article'):
            for elem in x.find_all('b'):
                company.append(elem.text.strip())
        while "" in company:
            company.remove('')
            
        for x in soup.find_all('article'):
            for y in x.find_all('section'):
                for elem in y.find_all('a'):
                    links_aux.append("https://acciontrabajo.ec"+elem['href'])

        for x in soup.find_all('article'):
            for y in x.find_all('section'):
                for elem in y.find_all('div',class_='v_detail detail'):
                    loc.append(elem.text.strip().upper())

    for elem in loc[::2]:
        locations.append(elem)
    for elem in links_aux:
            response = requests.get(api_adfocus+elem)
            b = response.content
            links.append(b.decode('utf-8'))

                    
    longitud = len(title)
    df = pd.DataFrame({'Nombre':title,'Empresa':company,'Localidad':locations,'Links':links,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]
    for elem in df.index:    
            requests.post(url_req+"{}\nEmpresa: {}\n{}{}\nLINK DE POSTULACIÓN:\n{}\nNOTA: {}".format(df['Nombre'][elem],df['Empresa'][elem],chr(128205),
            df['Localidad'][elem],df['Links'][elem],df['Nota'][elem]))
            time.sleep(5)
    formato_tiempo = datetime.datetime.now()
    hora = formato_tiempo.strftime("%H%M%S")


    with open('adfocus'+str(hora+'.txt'),'w') as f:
        for i in range(len(links)):
            if i<(len(links)-1):
                f.write("'"+links[i]+"',\n")
            else:
                f.write("'"+links[i]+"'\n")

scrap_accion()