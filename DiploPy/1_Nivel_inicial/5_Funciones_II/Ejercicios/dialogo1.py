from tkinter import *
from tkinter.messagebox import *


def mensaje_error():
    showerror("Titulo de mensaje de error", "Contenido del mensaje de error")


def verificar():
    if askyesno("Titulo de la consulta de verificacion", "Contenido de verificacion"):
        showinfo("Si", "Mensaje de informacion")
    else:
        showinfo("No", "Esta a punto de salir")


Button(text="Error", command=mensaje_error).pack(fill=X)
Button(text="Verificar", command=verificar).pack(fill=X)

mainloop()
