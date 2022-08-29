from tkinter import *

root = Tk()
root.title("Cartel")

label = Label(root, text=("Hola" + " Mateo " + "bienvenido" + "!"))
label.pack()

label2 = Label(root, text=(input("Hola Mateo bienvenido!")))
label2.pack()

root.mainloop()
