from bs4 import BeautifulSoup
import requests
from helium import start_chrome

url = 'https://reclutamiento.tia.com.ec'
#browser = start_chrome(url, headless=True)
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

title = list()

for elem in soup.find_all('div',class_='col-md-4'):
    for x in elem.find_all('h4'):
        for y in x.find_all('a'):
            title.append(y.text)


for elem in title:
    print(elem)