"""
a = 5
b = 6


def nopisa():
    a = 10
    print("La variable 'a' dentro de la función tiene por valor", a)
    print("'b' es global, por lo que puedo imprimirla acá", b)


nopisa()
print("La variable 'a' fuera de la función tiene por valor", a)
print("", end="\n################\n")
"""
#####################################
"""
a = 5


def funcion():
    print(a)


funcion()
"""
#####################################
"""
a = 5


def funcion():
    global a
    a = 10
    print(a)


funcion()
print(a)
"""
#####################################
"""
# #################################################
# Definir listas
# #################################################
juan = ["Juan Garcia", 24, 5000, "Pintor"]
susana = ["Susana Gomez", 25, 6000, "Empleada"]
print(juan[0])
# #################################################
# Definir lista como Base de datos
# #################################################
personas = [juan, susana]
# #################################################
# Imprimo elementos de la lista de base de datos
# #################################################
for x in personas:
    print(x)
print("------------------------------")
# #################################################
# Imprimo los apellidos y les doy aumento del 20%
# #################################################
for x in personas:
    print((x[0].split()[-1]))
    x[2] *= 1.20
for x in personas:
    print(x)
print("------------------------------")
# #################################################
# Agregamos un registro a la lista de base de datos
# #################################################
personas.append(["Pedro", 37, 7000, "Plomero"])
for x in personas:
    print(x)
print("------------------------------")
"""
#####################################
"""
lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]
# imprimimos la lista
print(lista)
print("", end="\n################\n")
# imprimimos elementos de primer nivel
for a in lista:
    print(a)
print("", end="\n################\n")
# imprimimos elementos de primer y segundo nivel
# con el if veo si el elemento de lista no es una lista
# si es una lista recorro la lista y sino paso al siguiente elemento
for a in lista:
    if isinstance(a, list):
        for b in a:
            print(b)
    else:
        print(a)
print("", end="\n################\n")
# imprimimos elementos de primer y segundo y tercer nivel
# con el if veo si el elemento de lista no es una lista
# si es una lista recorro la lista y sino paso al siguiente elemento
for a in lista:
    if isinstance(a, list):
        for b in a:
            if isinstance(b, list):
                for c in b:
                    print(c)
            else:
                print(b)
    else:
        print(a)
"""
#####################################
"""
lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]


def recorrer_lista(item, nivel):  # Agrego segundo parámetro
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print((""))
            print(x)


recorrer_lista(lista, 0)
"""
#####################################
"""
lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]


def recorrer_lista(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)


recorrer_lista(lista)
"""
#####################################
"""
lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]


def recorrer_lista(item, nivel):  # Agrego segundo parámetro
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print((""))
            print(x)


recorrer_lista(lista, 0)
"""
#####################################
"""
lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]


def recorrer_lista(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)


recorrer_lista(lista)
input("\n###########################\n")
"""
#####################################
"""
def contador_yield1(max):
    n = 0
    while n < max:
        yield n + 1


d = contador_yield1(3)
print(d)
print(end="\n###############\n")
print(next(d))
print(end="\n###############\n")
print(next(d))
print(end="\n###############\n")
print(next(d))
"""
