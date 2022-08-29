class Cliente:

    def __init__(self, usuario):
        self._usuario = usuario

    def getUsuario(self):
        print('Recupera el usuario...')
        return self._usuario

    def setUsuario(self, valor):
        print('Modifica el usuario...')
        self._usuario = valor

    def delUsuario(self):
        print('Remueve el usuario...')
        del self._usuario
    usuario = property(getUsuario, setUsuario, delUsuario, "Datos adicionales")

cliente1 = Cliente('Juan')
print(cliente1.usuario)
cliente1.usuario = 'Pedro'
print(cliente1.usuario)
del cliente1.usuario
print(Cliente.usuario.__doc__)
