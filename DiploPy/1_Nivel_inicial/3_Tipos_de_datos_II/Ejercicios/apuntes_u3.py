#####################################
# Crear sets y ejemplos de operaciones
#####################################
"""
set = {1, 2, 3, 4, 5, 3}
set1 = {10, 2, 13, 4, 15, 3, 1}
set2 = {10, 2, 13, 4, 15, 3}
print(set & set1)
print(set | set1)
print(set - set1)
print(set1 > set2)
"""
#######################################
# Usos de sets
#######################################
# Remover duplicados
#######################################
"""
lista1 = ["Manzana", "Pera", "Coco", "Pera", "Uva", "Banana", "Kiwi", "Coco"]
mi_set = set(lista1)
print(lista1)
print(mi_set)
lista2 = list(mi_set) #Remueve duplicados
print(lista2)
"""
#######################################
# Aplicación
#######################################
"""
socio = ["Juan", "Pedro", "Susana", "Anna", "Sofía", "Pablo"]
ajedrez = ["Pedro", "Susana", "Anna", "Sofía", "Pablo"]
natacion = ["Juan", "Pedro", "Susana"]

resultado = set(ajedrez).intersection(set(natacion))
print(resultado)
print(type(resultado))
"""
#######################################
# Formato de salida de datos
#######################################
"""
x = 1
y = 2
z = ["juan"]
print(x, y, z, sep="    ")
print(x, y, z, sep=", ")
print(x, y, z, sep=", ", end="!\n")
"""
#######################################
# Secuencia de datos COMPLETAR
#######################################
"""
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
"""
#######################################
# Formato literal (f-strings)
#######################################
"""
nombre = "Pedro"
edad = 40
print(f'{"fila":30}==>{nombre:10}{edad}')

valor = 3.141659
print(f"El valor {valor} redondeado a 3 dígitos luego de la coma queda: {valor:.3f}.")
"""
#######################################
# Dar formato con format()
#######################################
"""
votos = 42572654
voto_en_blanco = 43132495
porcentaje = (votos / (votos + voto_en_blanco)) * 100
print(
    "Los votos a favor son: {0} con un porcentaje de: {2:.2f}".format(
        votos, voto_en_blanco, porcentaje
    )
)
"""
#######################################
# pprint
#######################################
"""
import pprint

juan = {
    "identificacion": {"nombre": "Juan", "apellido": "Garcia"},
    "edad": 24,
    "sueldo": 5000,
    "profesión": "Pintor",
}
susana = {
    "identificacion": {"nombre": "Susana", "apellido": "Gomez"},
    "edad": 25,
    "sueldo": 6000,
    "profesión": "Empleada",
}
db = {}
db["juan"] = juan
db["susana"] = susana
print(db)
print("------------------------------")
pprint.pprint(db)
"""

"""
import pprint

mateo = {
    "id": {"nombre": "Mateo", "apellido": "Arcidiacono"},
    "edad": 18,
    "sueldo": 30000,
    "oficio": "Programador",
}
paula = {
    "id": {"nombre": "Paula", "apellido": "Oldano"},
    "edad": 45,
    "sueldo": 70000,
    "oficio": "Administrativa",
}
dic = {}
dic["mateo"] = mateo
dic["paula"] = paula
print(dic)
print("----------------------")
pprint.pprint(dic)
"""
#######################################
# Date
#######################################
"""
import datetime
import calendar

datetime.datetime.now()
print(datetime.datetime.utcnow())
print(datetime.datetime.now())
print(datetime.datetime.now().day)
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)
"""
# Abreviaciones
"""
import datetime
import calendar

print(datetime.datetime.today().strftime("%H:%M:%S--%d/%m/%y"))
"""

"""
%a - Nombre del día de la semana
%A - Nombre del día completo
%b - Nombre abreviado del mes
%B - Nombre completo del mes
%c - Fecha y hora actual
%d - Día del mes
%H - Hora (formato 24hs)
%I - Hora (formato 12hs)
%j - Día del año
%m - Mes en número
%M - Minutos
%p - Equivalente de AM o PM
%S - Segundos
%U - Semana del año (domingo como primer día de la semana)
%w - Día de la semana
%W - Semana del año (lunes como primer día de la semana)
%x - Fecha actual
%X - Hora actual
%y - Número de año (21)
%Y - Número de año entero (2021)
%Z - Zona horaria
"""
# Diferencia de fechas 1
"""
import datetime
import calendar

actual = datetime.datetime.now()
anterior = datetime.datetime(1975, 9, 15, 0, 0, 0)
print(actual - anterior)
"""

# Diferencia de fechas 2
"""
import datetime
import calendar

hoy = datetime.date.today()
hace5 = datetime.timedelta(days=5)
print(hoy)
print(hace5)
print(hoy - hace5)  # Resto 5 días
"""
#######################################
# GUI
#######################################
# Label
"""
from tkinter import *

master = Tk()
Label(text="uno").pack()
separador = Frame(master, height=2, bd=1, relief=SUNKEN)
separador.pack(fill=X, padx=5, pady=5)
Label(text="dos").pack()
mainloop()
"""
#######################################
# Grill & Sticky
#######################################
"""
from tkinter import *

root = Tk()
root.title("Identificacion")

Label(root, text="ID").grid(row=0, column=0, sticky=W)
Label(root, text="Nombre").grid(row=1, column=0, sticky=W)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()
"""
#######################################
# Botones y sus parámetros
#######################################
# Callback
"""
from tkinter import *

root = Tk()


def callback():
    print("click")


b = Button(root, text="OK", command=callback)
b.pack()
mainloop()
"""
# Para en una prueba desabilitar un botón le agrego state=DISABLED

# Padding
"""
from tkinter import *

master = Tk()


def callback():
    print("click")


b = Button(master, text="OK!", command=callback, padx=132, pady=132)
b.pack()
mainloop()
"""

# Alto y ancho
"""
from tkinter import *

master = Tk()

b = Button(master, text="Sure!", anchor=W, justify=LEFT, padx=22, height=3, width=12)
b.pack(fill=BOTH, expand=1)
mainloop()
"""

# Imagen
"""
from tkinter import *

master = Tk()

photo = PhotoImage(file="download.gif")
c = Button(master, text="Foto!", anchor=W, justify=LEFT, image=photo)
c.pack(fill=BOTH, expand=1)
mainloop()
"""

# Color

# Fondo: background="black" ó bg="black"
# Letra: foreground="red" ó fg="red"
# Fondo activa: activebackground="green"
# Letra activa: activeforeground="yellow"
# letra deashabilitado: disableforeground="blue"
"""
from tkinter import *

master = Tk()


def callback():
    print("click!")


b = Button(
    master,
    text="OK!",
    command=callback,
    padx=132,
    pady=132,
    activebackground="green",
    activeforeground="yellow",
    background="black",
    foreground="red",
)
b.pack()
a = Button(
    master,
    text="OK!",
    command=callback,
    padx=132,
    pady=132,
    background="black",
    disabledforeground="blue",
)
a.pack()
mainloop()
"""
#######################################
# Posición de texto/imagen y botón
#######################################

# Posición de texto e imagen
"""
anchor=SW

Opciones: N, NE, E, SE, S, SW, W, NW, o CENTER. Por default es CENTER. (anchor/Anchor)
"""

# Posicion del botón
"""
side=LEFT

Opciones: LEFT, TOP, RIGHT, BOTTOM
"""

"""
from tkinter import *

master = Tk()


master.geometry("300x300")


def callback():
    print("click")


b = Button(
    master,
    text="OK",
    command=callback,
    activebackground="green",
    activeforeground="yellow",
    background="black",
    foreground="red",
    height=7,
    width=12,
    anchor=SW,
)
b.pack(side=LEFT)
mainloop()
"""

# Tipo de texto
"""
font=("tipo", tamaño, "peso")
"""

"""
from tkinter import *

master = Tk()


def callback():
    print("ESOOO")


b = Button(
    master,
    text="OK",
    command=callback,
    anchor=W,
    justify=LEFT,
    padx=22,
    height=3,
    width=12,
    font=("courier", 22, "bold"),
)
b.pack(fill=BOTH, expand=1)
mainloop()
"""
