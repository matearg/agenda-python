import os

from xml.dom import minidom
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml1.xml" 
 
documento = minidom.parse(archivo)

varon = documento.getElementsByTagName('varon')
mujer = documento.getElementsByTagName('mujer')

print(varon[0].firstChild.data) 
print(varon[0].childNodes[0].data)
print(varon[0].attributes['edad'].value)
print(mujer[0].firstChild.data) 
print(mujer[0].childNodes[0].data)
print(mujer[0].attributes['edad'].value)