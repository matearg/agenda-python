def recorrerLista(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrerLista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)
