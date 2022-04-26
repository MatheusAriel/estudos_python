class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self, msg='oi'):
        print(f'{self.nome} está falando {msg} ClASSE({self.nome_classe})')


class Cliente(Pessoa):
    def falar(self):
        print('Estou falando na classe Cliente')

    def comprar(self):
        print(f'{self.nome} está comprando')


class ClienteVipe(Cliente):
    # sobree
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self, msg='Olá'):
        # esse super chama do primeiro pai, no caso aqui, cliente
        super().falar()

        # se quiser q chame o metodo falar de uma classe especifica
        Pessoa.falar(self)
        # ou
        # Cliente.falar(self)

        print(f'{self.nome.upper()} {self.sobrenome.upper()} está falando {msg}')
