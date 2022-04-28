from pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, idade: int, documento: str):
        super().__init__(nome, idade, documento)
        self._conta = None

    def exibir_dados_clientes(self):
        print('\n********************************')
        print(f'\tNome: {self.nome}')
        print(f'\tIdade: {self.idade}')
        print(f'\tDocumento: {self.documento}')
        print('*********************************', end='\n')

    def inserir_conta(self, conta):
        self._conta = conta

    @property
    def conta(self):
        return self._conta
