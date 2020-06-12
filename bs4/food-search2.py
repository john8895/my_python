# 引入內建 urllib
from urllib.request import urlopen
# 引入 BS4
from bs4 import BeautifulSoup

page = 59
while True:
    # 開啟網址
    response = urlopen('https://tabelog.com/tw/tokyo/rstLst/' + str(page) + '/?SrtT=rt')
    print('正在處理')
    try:


    # 將網址美化，要記得加第二個參數 html.parser 不然會報錯
    # 報錯不理也可，他會用他認為最好的解析器，這裡自動用了 html.parser
    html = BeautifulSoup(response)

    restaurant = html.find_all('li', class_='list-rst')

for r in restaurant:
    en = r.find('a', class_="list-rst__name-main")
    # print(en.text, en['href'])
    jp = r.find('small', class_='list-rst__name-ja')
    # print(jp.text)
    price = r.find_all(class_='c-rating__val')
    print(price[0].text, price[1].text, price[2].text, jp.text, en.text, en['href'])
