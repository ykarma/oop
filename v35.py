import re

s = r"\d+"

pattern = re.compile(s)

m = pattern.match("one12two23three33")

print(m)

print(m.group())
print(m.start(0))
print(m.span(0))