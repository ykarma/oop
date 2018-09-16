import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one12t3wo34three56")
print(m.group())

m = pattern.search("one12t3wo34three56", 10, 40)
print(m.group())