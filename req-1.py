import requests
import bs4

url = 'https://www.ptt.cc/bbs/EAseries/index.html'
my_headers = {'cookie': 'over18=1;'}
response = requests.get(url, headers=my_headers)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
# 輸出排版後的 HTML 程式碼
# print(soup.prettify())

# 網頁標題 HTML 標籤
title_tag = soup.title
# print(title_tag)

# 網頁的標題文字
# print(title_tag.string)

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
