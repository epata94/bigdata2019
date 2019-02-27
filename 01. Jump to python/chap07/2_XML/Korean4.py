from xml.etree.ElementTree import Element, parse

tree = parse("Korean3.xml")

root_node = tree.getroot()

print(root_node.items())
