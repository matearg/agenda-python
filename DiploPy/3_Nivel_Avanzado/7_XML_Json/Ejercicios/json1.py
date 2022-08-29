import os
import json
archivo = os.path.dirname(os.path.abspath(__file__))+"\\json1.json" 
archivo = json.loads(open(archivo).read())
print(archivo)
print("---"*25)
print(type(archivo))
print("---"*25)
print(type(archivo["autos"]))
print("---"*25)
print(type(archivo["autos"][0]))
print("---"*25)
print(archivo["autos"][0]["color"])
print("---"*25)