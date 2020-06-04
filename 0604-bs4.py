import requests
from bs4 import BeautifulSoup


url = 'https://www.ptt.cc/bbs/movie/M.1540692666.A.E90.html'
response = requests.get(url).text
html = BeautifulSoup(response, 'html.parser')

content = html.find('div', id='main-container')
values = content.find_all('span', class_='article-meta-value')
# print('作者：', values[0])
# print('看板：', values[1])
# print('文章標題：', values[2])
# print('發文時間：', values[3])


meta = content.find_all('div', class_='article-metaline')
# print('處理前')
# print('meta', meta)

for m in meta:
    print('m', m)
    m.extract()
print('處理後：=====')
print('meta', meta)



# meta = content.find_all('div', )