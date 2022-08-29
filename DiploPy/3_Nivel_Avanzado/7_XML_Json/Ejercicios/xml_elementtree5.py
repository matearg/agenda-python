import os
import xml.etree.ElementTree as ET
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml4.xml" 

import xml.etree.ElementTree as ET  
dom = ET.parse(archivo)  
raiz = dom.getroot()

# Agregamos elemento al elemento raíz
atributos = {}  
print(raiz[0])
etiqueta = raiz.makeelement('vehiculos_aereos', atributos)  
raiz.append(etiqueta)

# Agregamos elemento con atributo dentro del elemento creado en las líneas anteriores.
atributos2 = {'color': 'verde'}  
avion = raiz[0][1].makeelement('avion', atributos2)  
ET.SubElement(raiz[1], 'avion', atributos2)  
raiz[1][0].text = 'Este es un avión'

dom.write(archivo)  

