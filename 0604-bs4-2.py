import requests
from bs4 import BeautifulSoup


markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
# print(a_tag)

i_tag = soup.i.extract()
# print(i_tag)
# a_tag
# <a href="http://example.com/">I linked to</a>

# i_tag
# <i>example.com</i>

print(i_tag.parent)
# None