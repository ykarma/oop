import re

pattern = re.compile(r'\d+')

s = pattern.finditer("i am 18 years old and 185high")

print(type(s))

for i in s:
    print(i.group())