import re

patron = re.compile(r'(?P<etiqueta>[A-Z][A-Z0-9]*)\b[^>]*>.*?</(?P=etiqueta)')
string1 = "Prueba <B><I>Texto en negrita e italica</I></B> Esto solo es texto."

print(patron.search(string1))


"""
'B><I>Texto en negrita e italica</I></B'>
"""
