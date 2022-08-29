import os
import xml.etree.ElementTree as ET
archivo = os.path.dirname(os.path.abspath(__file__))+"\\xml2.xml" 

# Creamos cabecera
cabecera = '<?xml version="1.0" encoding="utf-8"?>'
# Creamos elementos raíz
raiz = ET.Element('mediolocomocion')  
vehiculo = ET.SubElement(raiz, 'vehiculo')  
moto = ET.SubElement(vehiculo, 'moto')  
auto = ET.SubElement(vehiculo, 'auto')  
# Creamos atributo
moto.set('marca','bmw')  
auto.set('marca','audi')  
moto.text = 'Moto número 1'  
auto.text = 'Auto número 1'

# creamos XML
datos = ET.tostring(raiz)  
datosstr = datos.decode("utf-8")
archivo = open(archivo, 'w')
archivo.write(cabecera)
archivo.write(datosstr)
archivo.close()