import re
p=re.compile('python',re.MULTILINE) #findall의 결과와 동일한 효과
dest_str="""python one python debug
life is too shrot
python two
you need python
python three
I will study python
"""
m = p.findall(dest_str)
print(m)