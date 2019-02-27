from xml.etree.ElementTree import parse

tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))
print(note.get("foo"))
print(note.get("foo","default"))
print(note.keys())
print(note.items())

from_tag = note.find("from")
print(from_tag.text)
from_tags = note.findall("from")
from_text = note.findtext("from")
print(from_text)
print("end")