import re

s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s, re.I)

m = pattern.match("Hello world wide web")

s = m.group(0)
print(type(s))
print(s)

a = m.span(0)
print(type(a))
print(a)

s = m.group(1)
print(type(s))
print(s)

a = m.span(1)
print(type(a))
print(a)

s = m.group()
print(type(s))
print(s)