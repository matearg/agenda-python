import os
import xml.etree.ElementTree as ET
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml4.xml" 

import xml.etree.ElementTree as ET  
dom = ET.parse(archivo)  
raiz = dom.getroot()

#Modificando una etiqueta por posición
print(raiz)
print(raiz[0])
print(raiz[0][0].text)
raiz[0][0].text = 'Moto modificada'
print(raiz[0][0].text)

#Modificando una etiqueta por nombre
for etiqueta in raiz.iter('auto'):  
    print(etiqueta.text)
    etiqueta.text = 'Moto modificada por segunda vez'
    print(etiqueta.text) 
    
#Agregar un atributo
for etiqueta in raiz.iter('auto'): 
    etiqueta.set('color', 'rojo')    
    
#Modificando un atributo
for etiqueta in raiz.iter('auto'):   
    etiqueta.set('color', 'azul')    

dom.write(archivo)
