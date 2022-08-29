class ControlMotor(type):
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
print(objeto.material)  # Accedo a atributo de superclae
print(objeto.color)  # Accedo a atributo de instancia
print(Auto.__dict__)  # Accedo a diccionario de atributos de clase
print(
    Auto.__dict__["marca"]
)  # Accedo a clave 'marca' del diccionario de atributos de clase
print(objeto.__dict__)  # Accedo a diccionario de atributos de instancia.
print(objeto.retornar_color(6))  # Acceso a método de instancia
print(Auto.__class__.encendido)  # Accedo a atributo 'encendido' de metaclase
print(Auto.encendido)  # Accedo a atributo 'encendido' de metaclase
try:
    print(objeto.encendido)
except AttributeError:
    print("La instancia no tiene acceso a este atributo")
print("---" * 25)
