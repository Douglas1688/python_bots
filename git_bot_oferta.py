import time as tiempo
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from helium import *
import os


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

def scrap_unmejorempleo():
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    chat_id="-1001458610971"
    #chat_id="1053185415"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="

    jobs = list()
    address = list()
    hour= list()
    links = list()
    links_aux= list()
    url = 'https://www.unmejorempleo.com.ec/busqueda_resultados.php?f=1'

    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    i = soup.find_all(class_='no-margin-top')
    h= soup.find_all(class_='text-warning')
    l = soup.find_all(class_='text-primary')


    for elem in i:jobs.append(elem.text.strip().upper())
    for elem in h:hour.append(elem.text.strip())
    for elem in l: address.append(elem.text.strip().upper())

    for p in soup.find_all(class_='no-margin-top'):
        for track in p.find_all('a'):
            links_aux.append('https://www.unmejorempleo.com.ec/'+track['href'])

    for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))


    longitud = len(jobs)

    df = pd.DataFrame({'Fuente':'Un mejor Empleo','Nombre':jobs,'Localidad':address,'Hora':hour,'Links':links,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]
        

    for elem in df.index:    
        requests.post(url_req+"{}\n{}\n{}{}\nFecha de Publicación:  {}\nLINK DE POSTULACIÓN:\n{}\nNOTA: {}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
        df['Localidad'][elem],df['Hora'][elem],df['Links'][elem],df['Nota'][elem]))
        tiempo.sleep(5)
    
def scrap_joraempleo():
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    chat_id="-1001458610971"
    #chat_id="1053185415"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="

    jobs = list()
    address = list()
    links = list()
    links_aux=list()
    for i in range(1,3):
        url = f'https://ec.jora.com/j?l=&p={i}&q=&since=lv&sp=recent_homepage&st=date&surl=0&tk=XSPdy1yZK16tDKJYL2HW-IXVwo91dxCbgmMurZwlN'
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        
        j = soup.find_all(class_='job-title')
        a= soup.find_all(class_='job-location')
        l = soup.find_all(class_='job-item')

        for elem in j:jobs.append(elem.text.strip().upper())
        for elem in a:address.append(elem.text.strip())
        for elem in l:links_aux.append('https://ec.jora.com'+elem['href'])

    for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))
   
    longitud = len(jobs)

    df = pd.DataFrame({'Fuente':'Jora Empleos','Nombre':jobs,'Localidad':address,'Links':links,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]        

    for elem in df.index:    
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}\nNOTA: {}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
        df['Localidad'][elem],df['Links'][elem],df['Nota'][elem]))
        tiempo.sleep(5)
     
def scrap_universo():  
    lst=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    today = datetime.datetime.today()

    d = '{:%d}'.format(today)
    m  = lst[int('{:%m}'.format(today))-1]
    y = '{:%Y}'.format(today)
    
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="
    
  
    url =f'https://www.eluniverso.com/clasificados/empleos/buscar?termino=&categoria=128562&fecha%5Bvalue%5D%5Bdate%5D={d}+{m}+{y}'

    headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
    
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'lxml')


    titulo = list()
    localidad = list()
    contenido = list()
    fecha = list()


    for i in soup.find_all('span',class_='titulo-clasificado'):
        titulo.append(i.text.upper())
    longitud = len(titulo)
    for i in range(longitud):
        localidad.append('GUAYAQUIL')
    for i in soup.find_all('div',class_='field-content'):
        contenido.append(i.text.replace('#','nº'))

    for i in soup.find_all('span',class_='fecha-clasificado'):
        fecha.append(i.text)
    longitud = len(titulo)

    df = pd.DataFrame({'Fuente':'Diario El Universo','Nombre':titulo,'Contenido':contenido,'Localidad':localidad,'Fecha':fecha},index=list(range(1,(longitud+1))))
    df = df.iloc[::-1]  

    for elem in df.index:
        requests.post(url_req+"{}\n{}\nDescripción:  {}\n{}{}\nFECHA:  {}\n".format(df['Fuente'][elem],df['Nombre'][elem],
            df['Contenido'][elem],chr(128205),df['Localidad'][elem],df['Fecha'][elem]))
        tiempo.sleep(5)

def scrap_multitrabajo():
    
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="


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

    for elem in links_aux:
            response = requests.get(api_adfocus+elem)
            b = response.content
            links.append(b.decode('utf-8'))


    longitud = len(title)
    df = pd.DataFrame({'Fuente':'Multitrabajos','Nombre':title,'Localidad':location,'Link':links,'Nota':'AL ABRIR EL LINK, ESPERA 6 SEGUNDOS Y PRESIONA SKIP'},index=list(range(1,(longitud+1))))

    for elem in df.index:
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}\n{}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
            df['Localidad'][elem],df['Link'][elem],df['Nota'][elem]))
        tiempo.sleep(5)

def scrap_ejob():
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    #chat_id="1053185415"
    chat_id="-1001458610971"
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

    for elem in links:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links_listos.append(b.decode('utf-8'))


    longitud = len(title)
   
    df = pd.DataFrame({'Fuente':'E-talent','Nombre':title,'Localidad':locations,'Link':links_listos},index=list(range(1,(longitud+1))))
    for elem in df.index:
        requests.post(url_req+"{}\n{}\n{}{}\nLINK DE POSTULACIÓN:\n{}".format(df['Fuente'][elem],df['Nombre'][elem],chr(128205),
       df['Localidad'][elem],df['Link'][elem]))
        tiempo.sleep(5)

def scrap_hiring(archivo):
        
    token="1463804463:AAG2QhbTkD_rLV0y0TWj3keuk5x--c3jz6I"
    #chat_id="1053185415"
    chat_id="-1001458610971"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="  
    api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url=" 
    #dir = 'C:/Users/GamaPrinter/PycharmProjects/python_bot/'
    dir = 'C:/Users/Administrator/Desktop/'
    lst=[]
    with open(dir+archivo,'r') as f:
        for elem in f:
            lst.append(elem.replace('\n',''))
    title = list()
    company =list()
    links = list()
    links_aux = list()
    locations = list()

    for z in range(len(lst)):
        i=0
        url = 'https://'+lst[z]+'hiringroom.com/jobs'

        browser = start_chrome(url,headless=True)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for x in soup.find_all('div',class_='col-md-12'):
            for elem in x.find_all('h2'):
                title.append(elem.text.strip().upper())
                i+=1

        for x in soup.find_all('li',class_='vacantes'):
            for elem in x.find_all('a'):
                links_aux.append('https:'+elem['href'])

        for x in soup.find_all('li',class_='vacantes'):
            for elem in x.find_all('p',class_='location'):
                locations.append(elem.text.upper())
        for _ in range(i):
            company.append(lst[z].upper())
        os.system('taskkill /f /im chrome.exe')
        

    
    for elem in links_aux:
        response = requests.get(api_adfocus+elem)
        b = response.content
        links.append(b.decode('utf-8'))

    longitud = len(title)   

    df = pd.DataFrame({'Nombre':title,'Empresa':company,'Localidad':locations,'Link':links},index=list(range(1,(longitud+1))))
    for elem in df.index:
        requests.post(url_req+"{}\nEmpresa: {}\n{}{}\nLINK DE POSTULACIÓN:\n{}".format(df['Nombre'][elem],df['Empresa'][elem],chr(128205),df['Localidad'][elem],df['Link'][elem]))
        tiempo.sleep(5)



while True:
    formato_tiempo = datetime.datetime.now()
    hora = formato_tiempo.strftime("%H:%M:%S")
    if hora == '18:57:00' or hora =='23:00:00':        
        scrapp_compu()       
    elif hora == '21:33:00':
        scrap_unmejorempleo()       
    elif hora == '12:44:00':
        scrap_joraempleo()    
    elif hora == '21:00:00':
        scrap_multitrabajo()
    elif hora == '13:00:00':
        scrap_ejob()
    elif hora=='12:00:00':
        scrap_hiring('hir1.txt')
    elif hora == '14:00:00':
        scrap_hiring('hir2.txt')
    elif hora == '16:00:00':
        scrap_hiring('hir3.txt')
    elif hora == '18:00:00':
        scrap_hiring('hir4.txt')
    elif hora == '19:00:00':
        scrap_hiring('hir5.txt')
    elif hora == '20:00:00':
        scrap_hiring('hir6.txt')
    elif hora =='22:00:00':
        scrap_hiring('hir7.txt')
    elif hora =='00:00:00':
        scrap_hiring('hir8.txt')
    elif hora =='02:00:00':
        scrap_hiring('hir9.txt')
    elif hora =='03:00:00':
        scrap_hiring('hir10.txt')


    