from urllib.request import urlopen
import ssl
import json

response = urlopen("https://www.google.com/doodles/json/2020/6?hl=zh_TW")
doodles = json.load(response)
print(doodles)