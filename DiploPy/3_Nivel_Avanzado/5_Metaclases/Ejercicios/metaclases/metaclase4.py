class Material:
    pass


class Auto(Material):
    color = "azul"

    def retornar_color(self, color):
        return self.color


objeto = Auto()
print(type(objeto))
print(type(Auto))
print(type(Auto.__class__))

print("---" * 25)

Auto2 = type(
    "Auto2", (Material,), {"color": "azul", "retornar_color": (lambda x: x.color)}
)
objeto2 = Auto2()
print(Auto2)
print(objeto2)
print(objeto2.color)
print(objeto2.retornar_color())
print(type(objeto2))
print(type(Auto2))
print(type(Auto2.__class__))
