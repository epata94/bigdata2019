import re
p=re.compile('[a-c]')
m = p.match("a")
print(m) # 매칭이 된다
p=re.compile('[a-c]')
m = p.match("b")
print(m) # 매칭이 된다
p=re.compile('[a-c]')
m = p.match("c")
print(m) # 매칭이 된다
p=re.compile('[1-3]')
m = p.match("1")
print(m) # 매칭이 된다
p=re.compile('[1-3]')
m = p.match("2")
print(m) # 매칭이 된다
p=re.compile('[1-3]')
m = p.match("3")
print(m) # 매칭이 된다
