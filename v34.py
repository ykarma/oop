from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,'lxml')

content = soup.prettify()
#print(content)
print("==" * 12)

#print(soup.head)
print("==" * 12)
#print(soup.meta)
print("==" * 12)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)