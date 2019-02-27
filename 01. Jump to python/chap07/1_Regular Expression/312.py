import re

# p = re.compile('\\\section')
# p = re.compile(r'\') # Error
p=re.compile(r'\\')
print(p.search("\section"))
p = re.compile(r'\\section')
print(p.search("\\\\section"))
p = re.compile(r'\\')
print(p.search("\\\\section"))

p= re.compile(r'\bclass')
print(p.search(' class'))
p= re.compile('\b')
print(p.search('\b'))

