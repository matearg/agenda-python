class Control(type):
    estado = "inspección"


class ControlMotor(Control):
    encendido = False


class Material:
    material = "plástico"


class Auto(Material, metaclass=ControlMotor):

    marca = "renault"

    def __init__(self, color):
        self.color = color

    def retornar_color(self, valor):
        return self.color + str(valor)


objeto = Auto("azul")
print(Auto.__class__.estado)  # Accedo a atributo 'estado' de metaclase padre
print(Auto.__class__.encendido)  # Accedo a atributo 'encendido' de metaclase
print(Auto.__class__)
