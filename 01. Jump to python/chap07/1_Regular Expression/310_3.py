import re
# p=re.compile('^python\s\w+')
p=re.compile('\w+\spython$',re.MULTILINE)
dest_str="""python one python debug
life is too shrot
python two
you need python
python three
I will study python
"""
m = p.findall(dest_str)
print(m)