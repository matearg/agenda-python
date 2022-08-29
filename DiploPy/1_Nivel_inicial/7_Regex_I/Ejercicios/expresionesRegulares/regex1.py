import re

patron = re.compile('[p+]')
lista = ['+pera', 'vfg']

print(patron.match(lista[0]))
print(patron.match(lista[1]))

if not patron.match(lista[0])is None:
    print('El resultado no es None')

if patron.match(lista[0])is not None:
    print('El resultado no es None')
    
    
if patron.match(lista[1])is None:
    print('El resultado es None')

input()
