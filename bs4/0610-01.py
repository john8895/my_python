from urllib.request import urlopen
import ssl
import json

response = urlopen("https://www.google.com/doodles/json/2020/6?hl=zh_TW")
doodles = json.load(response)
print(doodles)

# https://edu.tcfst.org.tw/edm/08C009/images/Python%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%20.pdf
# page 38

