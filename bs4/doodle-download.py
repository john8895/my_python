"""
1. 引入必要套件
 1.1 urllib 中的 urlopen
 1.2 json
2. 開啟網址
3. 將資料轉為 json
4. 輸出資料
    4.1 將資料存入序列
"""

from urllib.request import urlopen, urlretrieve
import json
import sys
import os

# 開啟網址
# response = urlopen("https://www.google.com/doodles/json/2020/6?hl=zh_TW")
# doodles = json.load(response)

if not os.path.exists("doodles"):
    os.mkdir("doodles")

for m in range(1, 13):
    url = "https://www.google.com/doodles/json/2018/" + str(m) + "?hl=zh_TW"
    print("處理月份:", url)
    response = urlopen(url)
    doodles = json.load(response)
    for d in doodles:
        url = "https:" + d['url']
        title = d['title']
        dirname = 'doodles/' + str(m)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        fpath = dirname + '/' + url.split('/')[-1]
        urlretrieve(url, fpath)

# for d in doodles:
#     url = "https:" + d["url"]
#     title = d["title"]
#     fpath = "doodles/" + url.split("/")[-1]
#     urlretrieve(url, fpath)
#     # print(url.split("/")[-1])
#     # print("url".split('/'))
#     # print("圖片標題:", title)
#     # print("圖片網址:", url)
