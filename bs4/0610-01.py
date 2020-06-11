"""
1. 引入必要套件
 1.1 urllib 中的 urlopen
 1.2 json
2. 開啟網址
3. 將資料轉為 json
4. 輸出資料
    4.1 將資料存入序列

"""
# https://edu.tcfst.org.tw/edm/08C009/images/Python%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%20.pdf
# page 38

from urllib.request import urlopen, urlretrieve
import json
import sys

# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
#
# json_str = json.dumps(data)  # 編碼：轉為字串
# json = json.loads(json_str)  # 解碼：轉為字典
# print(json_str)
# print(type(json_str))
# sys.exit()

"""
json.dump => 編碼：將 json 字典轉為字串
json.loads => 解碼：將 json 編碼的字串轉為字典
"""

# 開啟網址
response = urlopen("https://www.google.com/doodles/json/2020/6?hl=zh_TW")
# sys.exit() # 中斷程式
# json.load =>
doodles = json.load(response)

for d in doodles:
    url = "https:" + d["url"]
    title = d["title"]
    fpath = "doodles/" + url.split("/")[-1]
    urlretrieve(url, fpath)
    # print(url.split("/")[-1])
    # print("url".split('/'))
    # print("圖片標題:", title)
    # print("圖片網址:", url)
