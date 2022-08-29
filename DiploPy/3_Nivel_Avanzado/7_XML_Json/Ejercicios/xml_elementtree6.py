import os
import xml.etree.ElementTree as ET
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml4.xml" 

import xml.etree.ElementTree as ET  
dom = ET.parse(archivo)  
raiz = dom.getroot()

raiz[0][1].attrib.pop('color', None) 
raiz[0].remove(raiz[0][0])
dom.write(archivo)  

