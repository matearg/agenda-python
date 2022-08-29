class MiMetaclase(type):
    def __new__(meta, nombre_de_clase, superclase, diccionario_de_clase):
        print('En new de metaclase:', meta, nombre_de_clase, superclase, diccionario_de_clase, sep='\n...')
        return type.__new__(meta, nombre_de_clase, superclase, diccionario_de_clase)

class MiSuperclase:
    pass
    
class MiClase1(MiSuperclase, metaclass=MiMetaclase):

    atributo1 = 1           
    def metodo1(self, arg):          
        return self.atributo1 + 3*arg

print('Creando una instancia') 
X = MiClase1() 
print('atributo1:', X.atributo1, X.metodo1(7))

    
