class Evaluar:
    def __init__(self):
        self._valor1 = 0
        self._valor2 = 0
        self._valor3 = 0
        self._valor4 = 0
        self._valor5 = 0
        self._valor6 = 0
        self._valor7 = 0
        
    @property
    def valor1(self):
        return self._valor1

    @valor1.setter
    def valor1(self, valor):
        self._valor1 = valor if valor % 2 == 0 else 0

    @property
    def valor2(self):
        return self._valor2

    @valor2.setter
    def valor2(self, valor):
        self._valor2 = valor if valor % 2 == 0 else 0

    @property
    def valor3(self):
        return self._valor3

    @valor3.setter
    def valor3(self, valor):
        self._valor3 = valor if valor % 2 == 0 else 0

    @property
    def valor4(self):
        return self._valor4

    @valor4.setter
    def valor4(self, valor):
        self._valor4 = valor if valor % 2 == 0 else 0

    @property
    def valor5(self):
        return self._valor5

    @valor5.setter
    def valor5(self, valor):
        self._valor5 = valor if valor % 2 == 0 else 0

    @property
    def valor6(self):
        return self._valor6

    @valor6.setter
    def valor6(self, valor):
        self._valor6 = valor if valor % 2 == 0 else 0
        

    @property
    def valor7(self):
        return self._valor7

    @valor7.setter
    def valor7(self, valor):
        self._valor7 = valor if valor % 2 == 0 else 0    
        
el_valor = Evaluar()
el_valor.valor1 = 1
el_valor.valor2 = 2
el_valor.valor3 = 3
el_valor.valor4 = 4
el_valor.valor5 = 5
el_valor.valor6 = 6
el_valor.valor7 = 7
print(el_valor.valor1)
print(el_valor.valor2)
print(el_valor.valor3)
print(el_valor.valor4)
print(el_valor.valor5)
print(el_valor.valor6)
print(el_valor.valor7)