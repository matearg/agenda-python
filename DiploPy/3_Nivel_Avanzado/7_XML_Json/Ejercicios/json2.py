import os
import json
archivo = os.path.dirname(os.path.abspath(__file__))+"\\json2.json" 

data = {}
data['persona'] = []

data['persona'].append({
    'nombre': 'Cecila',
    'apellido': 'Rodriguez',
    'age': 54,
    })

data['persona'].append({
    'nombre': 'Cecila',
    'apellido': ['Rodriguez', 'Garcia'],
    'age': 54,
    })

with open(archivo, 'w') as file:
    json.dump(data, file, indent=4)