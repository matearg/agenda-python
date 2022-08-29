class RaizCuadrada:
    def __init__(self, A):

        self.A = A
        self.n = len(self.A)
        self.longitud = len(self.A)

    def __iter__(self):
        # bucle for pra ordenar
        for i in range(self.n - 1):
            for j in range(self.n - 1):
                if self.A[j] > self.A[j + 1]:
                    aux = self.A[j]
                    self.A[j] = self.A[j + 1]
                    self.A[j + 1] = aux

        for valor in range(0, self.longitud):
            yield self.A[valor] ** 0.5


A = [81, 16, 64, 9]
x = RaizCuadrada(A)
p = iter(x)
print(next(p), next(p), next(p))
for i in RaizCuadrada(A):
    print(i, end=" ")
