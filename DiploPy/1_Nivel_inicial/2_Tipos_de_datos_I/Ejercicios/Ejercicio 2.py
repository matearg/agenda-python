from tkinter import *

frutas = ["peras", "uvas"]

root = Tk()
root.title("Frutas Favoritas")

label = Label(
    root, text="Mis frutas favoritas son las " + frutas[0] + " y las " + frutas[1] + "."
)
label.pack()

root.mainloop()
