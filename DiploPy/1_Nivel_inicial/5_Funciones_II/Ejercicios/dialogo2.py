from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Dialogo")


def verificar():
    if askyesno("Verificacion", "Desea realizar una verificacion"):
        showinfo("Verificacion", "Se ha verificado correctamente")
    else:
        showinfo("Verificacion", "Esta a punto de salir")


Button(
    text="Error", command=(lambda: showerror("Error", "Se ha producido un error"))
).pack(fill=X)
Button(text="Verificar", command=verificar).pack(fill=X)

root.mainloop()
