import re


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # get
    @property
    def preco(self):
        return self._preco

    # set
    @preco.setter
    def preco(self, value):
        if not isinstance(value, float):
            value = value.replace('R$', '').replace(' ', '')
            value = float(value)
        self._preco = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value.title()

    def descontar(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


p1 = Produto('CAMISETA', 50.00)
print(p1.__dict__)
p1.descontar(50)
print(p1.preco)

print()
p2 = Produto('CANECA', 'R$35.90')
print(p2.__dict__)
p2.descontar(50)
print(p2.preco)
