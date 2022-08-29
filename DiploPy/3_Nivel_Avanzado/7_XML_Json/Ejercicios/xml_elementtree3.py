import os
import xml.etree.ElementTree as ET
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml3.xml" 

import xml.etree.ElementTree as ET  
dom = ET.parse(archivo)  
raiz = dom.getroot()

# find the first 'item' object
for etiqueta in raiz:  
    print(etiqueta.find('auto').get('marca'))
print('---'*25)   
for etiqueta in raiz:
    for sub_etiqueta in etiqueta.findall('auto'):
        print(sub_etiqueta.attrib)
        print(sub_etiqueta.get('marca'))