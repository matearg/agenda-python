class MiSingleton(object):
    class __MiSingleton:
        def __init__(self):
            self.usuario = None
            # print(str(self))

        def __str__(self):
            return repr(self) + " - " + self.usuario

        def imprimir(self):
            print("hola")

    instancia = None

    def __new__(cls):
        if not MiSingleton.instancia:
            MiSingleton.instancia = MiSingleton.__MiSingleton()
        return MiSingleton.instancia


juan = MiSingleton()
juan.usuario = "Juan Perez2"
print(juan)
print(juan.imprimir())

pedro = MiSingleton()
pedro.usuario = "Pedro Correas"
print(pedro)
Ana = MiSingleton()
Ana.usuario = "Ana Gomez"
print(Ana)
