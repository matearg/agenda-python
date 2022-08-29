from tkinter import *

root = Tk()

root.title("Yo soy una pantalla comun")
entrada = Entry()
entrada.pack(fill=BOTH, anchor=CENTER, expand=TRUE)
boton1 = Button(text="No hago nada", command=NONE)
boton1.pack(fill=NONE, anchor=S, expand=TRUE)

mainloop()
