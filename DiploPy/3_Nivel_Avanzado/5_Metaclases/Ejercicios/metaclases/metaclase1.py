def extenter_clase(self, arg):
    print(arg)


class MiClase1:
    pass


MiClase1.extenter_clase = extenter_clase

objeto = MiClase1()
objeto.extenter_clase("Este método se ha agregado a la clase")

print("---" * 20)
print(type(MiClase1))