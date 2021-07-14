"""
The AdFoc.us API allows programmers to implement short URLs into their software and applications.
Here is your account's custom API access URL:
http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url=http://www.google.com/

The only required variable to send is url= which contains the full URL of the link to shrink.

If there is NO error, the API will return an AdFoc.us shortened URL.
If there is an error, the API will return 0."""
"""
import requests

url='https://github.com/n0shake/Public-APIs'
api_adfocus = "http://adfoc.us/api/?key=d3be1cc8976b84b2b9257f6b29608c36&url="

response = requests.get(api_adfocus+url)
b = response.content
print(b.decode('utf-8'))"""
"""
import requests
url="https://www.computrabajo.com.ec/ofertas-de-trabajo/oferta-de-trabajo-de-tecnico-de-calidad-qa-duran-en-duran-9A2542C10A3CAC2161373E686DCF3405"
api_tiny = f"https://tinyurl.com/api-create.php?url={url}"

response = requests.get(api_tiny+url)
b =  response.content
link =  b.decode('utf-8')
print(link)
"""
"""
cont = 1
while cont<=3: 
    try:
        var =eval(input('Ingrese: '))
        if isinstance(var,int):print('Entero')
        elif isinstance(var,float):print('Decimal')
        break    
    except:
        
        print(f'Dato no numérico,tienes {(3-cont)} intentos.')
        cont+=1
else:print('Perdiste')

"""



