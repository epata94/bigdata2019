import re
original_text="""1a dkfjsjkflsdjflsdjflsdfkj
b3 dkfjskdlfjslfjlsjfl
3k dkjflskdjfklsdjkfl
5j djkfjsklfjsljfsjdfljsdlf
k4 dkjfkdjfldsfjllfs
9p djkfdjsf
u9 djkfjksdjfsljfdslfjl
"""
# p=re.compile('1a [a-z]+.b3')
p=re.compile('1a [a-z]+.b3', re.DOTALL)
m = p.match(original_text)
print(m) 
