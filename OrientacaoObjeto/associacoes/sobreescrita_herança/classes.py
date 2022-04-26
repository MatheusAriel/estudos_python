class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self, msg='oi'):
        print(f'{self.nome} está falando {msg} ClASSE({self.nome_classe})')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando')
