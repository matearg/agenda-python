class Personas:
    def comerArroz(self):
        self.accion()


class Chinos(Personas):
    def accion(self):
        print("Los chinos comen arroz con palillos")


x = Chinos()
x.comerArroz()
