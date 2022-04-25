class Pessoa:
    def __init__(self, nome):
        # assim esta acessando o atributo nome
        # self._nome = nome
        # assim estou chamando o setter nome
        self.nome = nome

    @property
    def nome(self):
        print('Getter foi executado')
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('setter foi executado')
        self._nome = nome.upper()

    @property
    def sobrenome(self):
        return 'Souza'


p1 = Pessoa('Marcos')
print(p1.nome, p1.sobrenome)

"""
#da erro pois agr o nome é um get e não mais uma função, seria como acessar o atributo da classe
print(p1.nome())
"""
print()
p1.nome = 'Matheus'
print(p1.nome)
