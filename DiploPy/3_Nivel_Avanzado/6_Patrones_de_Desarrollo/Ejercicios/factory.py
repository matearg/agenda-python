def factory(Clase, *pargs, **kargs):
    return Clase(*pargs, **kargs)

class Auto:
    def doit(self, mensaje):
        print(mensaje)

class Moto:
    def __init__(self, color, marca='Fiat'):
        self.color = color
        self.marca = marca

if __name__ == '__main__':
    object1 = factory(Auto)
    object2 = factory(Moto, "Azul", "Chevrolet")
    object3 = factory(Moto, color='Roja')

    object1.doit('Tipo de auto')
    print(object2.color, object2.marca)
    print(object3.color, object3.marca)
