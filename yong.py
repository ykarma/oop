from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,'lxml')

content = soup.prettify()
print(content)