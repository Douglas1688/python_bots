import time
import webbrowser
import os


url = 'https://youtu.be/5Vam-OsTiGY'

for i in range(30):
    webbrowser.open(url)
    time.sleep(10)
os.system('TASKKILL /F /IM chrome.exe')

