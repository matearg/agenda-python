from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from modelo import Abmc


class VistaApp:
    def __init__(self, window):
        self.root = window
        self.a_val = StringVar()
        w_ancho = 20
        self.root.title("Mi app")
        self.entrada1 = Entry(self.root, textvariable=self.a_val, width=w_ancho)
        self.entrada1.grid(row=1, column=1)
        b1 = Button(self.root, text="Alta", command=lambda: self.para_alta(self.a_val))
        b1.grid(row=6, column=1)
        self.objeto_m = Abmc()

    def para_alta(self, param1):
        self.objeto_m.alta(param1.get())
