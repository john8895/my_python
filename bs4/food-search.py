from urllib.request import urlopen
from bs4 import BeautifulSoup

reponse = urlopen('https://tabelog.com/tw/tokyo/rstLst/?SrtT=rt')
html = BeautifulSoup(reponse, 'html.parser')
print(html)