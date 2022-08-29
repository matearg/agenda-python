A = [81, 16, 64, 9]

iterador = iter(A)
try:
    while True:
        print(iterador.__next__())

except StopIteration:
    print("Hemos llegado al final de la lista.")
