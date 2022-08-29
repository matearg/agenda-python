import os
import xml.etree.ElementTree as ET  
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml1.xml" 

diagrama = ET.parse(archivo)  
elementoRaiz = diagrama.getroot()
print(elementoRaiz)
print(elementoRaiz[0].text)
print(elementoRaiz[0].attrib)
print(elementoRaiz[0].attrib['edad'])
print(elementoRaiz[1].text)
print(elementoRaiz[1].attrib)
print(elementoRaiz[1].attrib['edad'])