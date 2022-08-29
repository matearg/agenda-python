from tkinter import *

frutas = ["pera", "banana", "manzana", "uva", "mandarina", "naranja", "kiwi"]

root = Tk()

root.title("Mejor Fruta")

label = Label(root, text=frutas[2])

label.pack()

root.mainloop()
