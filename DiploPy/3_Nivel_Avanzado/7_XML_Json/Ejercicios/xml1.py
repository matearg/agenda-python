import os

from xml.dom import minidom
archivo1 = os.path.dirname(os.path.abspath(__file__))+"\\xml1.xml" 
# parse an xml file by name
mydoc = minidom.parse(archivo1)

items = mydoc.getElementsByTagName('varon')

# one specific item attribute
print(items[0].firstChild.data) 
print(items[0].childNodes[0].data)
print(items[0].attributes['edad'].value)

