class ControlMotor(type):
    def retornar_material(cls):
        return "Retornar material"


class Auto(metaclass=ControlMotor):
    pass


print(Auto.retornar_material())
objeto = Auto()
try:
    print(objeto.retornar_material())
except:
    print("La instancia no tiene acceso a este método")
