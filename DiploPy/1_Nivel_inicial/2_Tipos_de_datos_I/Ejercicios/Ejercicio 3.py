from tkinter import *

datos = {
    "identificador": {"apodo": "Mate"},
    "nombre": "Mateo",
    "apellido": "Arcidiacono",
    "telefono": "123-7890",
}

root = Tk()
root.title("Datos")

label = Label(root, text=len(datos))
label.pack()

label2 = Label(root, text=list(datos.keys()))
label2.pack()

root.mainloop()
