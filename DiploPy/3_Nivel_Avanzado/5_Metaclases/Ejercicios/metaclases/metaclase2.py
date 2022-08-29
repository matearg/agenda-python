def extenter_clase(self, arg):
    print(arg)


def nueva_funcionalidad(Clase):
    Clase.extenter_clase = extenter_clase


class MiClase1:
    pass


nueva_funcionalidad(MiClase1)

objeto = MiClase1()
objeto.extenter_clase("Este método se ha agregado a la clase")

print("---" * 20)
