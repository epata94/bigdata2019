import re
original_text="""dkfjlsdfa
 bdfdkfslf"""
# p=re.compile("[a-z]*. [a-z]*")
# p=re.compile("[a-z]*. [a-z]*", re.DOTALL)
p=re.compile("[a-z]*. [a-z]*", re.S)
m = p.match(original_text)
print(m) 
