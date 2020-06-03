import re

import requests
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我是網頁標題</title>
</head>
<body>
<p class="title">
    <b>sdasdassd</b>
</p>
<a href="http://www.google.com.tw" class="sister" id="link1">john</a>
<a href="http://www.yahoo.com.tw" class="sister" id="link2">john</a>
<a href="http://www.kimo.com.tw" class="sister" id="link3">john</a>;Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa cupiditate distinctio, doloremque eos excepturi, libero maiores, perferendis perspiciatis quo sapiente soluta temporibus vel voluptate. Alias delectus iure nemo qui sint.
<p class="story">....</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print('獲取所有的連結')
# links = soup.find_all('a')
# for link in links:
#     print(link.name, link['href'], link.text)
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.text)

print('獲取指定的連結')
# link_node = soup.find('a', href='http://www.google.com.tw')
# print(link_node.name, link_node['href'], link_node.text)
link_node = soup.find('a', href='http://www.kimo.com.tw')
print(link_node.name, link_node['href'], link_node.text)

# print('正則匹配')
# link_node2 = soup.find(href=re.compile("/.*[kimo].*/"))
# print(link_node2)

# 輸出排版後的 HTML 程式碼
# print(soup.prettify())

# 網頁標題 HTML 標籤
# title_tag = soup.title
# print(title_tag)
title_tag = soup.title
print(title_tag)

# 網頁的標題文字
# print(title_tag.string)
print('網頁的標題文字:', title_tag.string)

# 搜尋所有超連結與粗體字
# tags = soup.find_all(["a", "b"])
# print(tags)


# 限制搜尋結果數量
# tags = soup.find_all(["a", "b"], limit=2)
# print(tags)

# 只抓出第一個符合條件的節點
# a_tag = soup.find("a")
# print(a_tag)

# 不使用遞迴搜尋，僅尋找次一層的子節點
# soup.html.find_all("title", recursive=False)

# 根據 id 搜尋
# link2_tag = soup.find(id='link2')
# print(link2_tag)

# 搜尋 href 屬性為 /my_link1 的 a 節點
# a_tag = soup.find_all("a", href="/my_link1")
# print(a_tag)

# 以正規表示法比對超連結網址
# import re
# links = soup.find_all(href=re.compile("^/my_link\d"))
# print(links)

# a_tags = soup.find_all('a')
# for tag in a_tags:
    # print(tag.string)
    # print(tag.get('href'))


# articles = soup.find_all('div', 'title a')
# print(articles)
# titles = soup.find_all('div', 'title')
# for t in titles:
#     print(t.text)