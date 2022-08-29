# ################################################
# Por posición #####
# ################################################
"""
def f(x, y, z):
    print(x, y, z)


f(1, 2, 3)
print("", end="\n#####################\n")
"""
# ################################################
# Por nombre #####
# ################################################
"""
def f(x, y, z):
    print(x, y, z)


f(z=3, y=2, x=1)
print("", end="\n#####################\n")
"""
# ################################################
# Por mixto - primero de izquierda a derecha ##
# y luego por nombre ####
# ################################################
"""
def f(x, y, z):
    print(x, y, z)


f(1, z=3, y=2)
print("", end="\n#####################\n")
"""
# #########################################################
# Si usamos * podemos pasar tuplas y listas a una función #
# #########################################################
"""
def f(a, *args):
    print("Tupla de valores:", args)
    for arg in args:
        print("Elemento de la tupla:", arg)


f(0, 1, 2, "Manzana")
"""
# ##############################################################
# Si usamos ** python interpreta los datos como un diccionario #
# ##############################################################
"""
def funcion(**kwargs):
    if kwargs is not None:
        for clave, valor in kwargs.items():
            print("%s == %s" % (clave, valor))


funcion(nombre="Mateo", edad=18, sexo="Masculino")
print(type(funcion))
"""
# ################################################
# Recursividad #####
# ################################################
"""
def misuma(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + misuma(L[1:])


print(misuma([1, 2, 3, 4, 5]))
"""
# ################################################
# Conseguir la suma con función ternaria ##
# ################################################
"""
def miSuma(L):
    return 0 if not L else L[0] + miSuma(L[1:])


print(miSuma([1, 2, 3, 4, 5]))
"""
# ################################################
# El mismo programa con dos funciones ##
# ################################################
"""
def misuma(L):
    if not L:
        return 0
    return no_vacia(L)


def no_vacia(L):
    return L[0] + misuma(L[1:])


print(misuma([1.1, 2.2, 3.3, 4.4, 5.5]))
"""
# ################################################
#
# ################################################
