"""lst=list()
with open('C:/Users/GamaPrinter/PycharmProjects/python_bot/hir.txt','r') as f:
    for elem in f:
        lst.append(elem.replace('\n',''))

lst_new = []
for elem in lst:
    if elem not in lst_new:
        lst_new.append(elem)

print(len(lst))
print(len(lst_new))

with open('C:/Users/GamaPrinter/PycharmProjects/python_bot/new_hir.txt','w') as f:
    for elem in lst_new:
        f.write(f'{elem}\n')"""

import pyshorteners
s = pyshorteners.Shortener(api_key='2809993801ceb0ea8d0b0dcfd07537d1e19c3571')
print(s.bitly.short('https://www.google.com'))
print(s.bitly.short('https://www.claro.com.ec'))
