# 引入熊貓
import pandas as pd
# 引入內建 urllib
from urllib.error import HTTPError
from urllib.request import urlopen
# 引入 BS4
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

pd.DataFrame(columns=['總合評分'])

# 步驟：
# df = pd.DataFrame(columns=['a', 'b'])
# s = pd.Series([資料1, 資料2], index=['a', 'b'])
# df = df.append(s, ignore_index=True)
# df.to_csv('.csv', encoding='utf-8', index=False)

page = 59
while True:
    # 開啟網址
    url = 'https://tabelog.com/tw/tokyo/rstLst/' + str(page) + '/?SrtT=rt'
    print('正在處理', url)
    try:
        response = urlopen(url)
    except HTTPError:
        print('[完成] 應該是來到最後一頁了')
        break

    # 將網址美化，要記得加第二個參數 html.parser 不然會報錯
    # 報錯不理也可，他會用他認為最好的解析器，這裡自動用了 html.parser
    html = BeautifulSoup(response)
    restaurant = html.find_all('li', class_='list-rst')

    for r in restaurant:
        en = r.find('a', class_="list-rst__name-main")
        jp = r.find('small', class_='list-rst__name-ja')
        price = r.find_all(class_='c-rating__val')
        print(price[0].text, price[1].text, price[2].text, jp.text, en.text, en['href'])

    page = page + 1