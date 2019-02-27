from xml.etree.ElementTree import parse
# import xml.etree.ElementTree as ET

tree=parse("Korean3.xml")
root_node=tree.getroot()

print(root_node.find('data').text)
data = root_node.find('data')
print(data.text)

