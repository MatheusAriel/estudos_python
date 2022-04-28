class Banco:
    def __init__(self, nome, agencias):
        self._nome = nome
        self._clientes = []
        self._contas = []
        self._agencias = agencias

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.upper()

    def inserir_cliente(self, cliente):
        if self._clientes:
            for c in self._clientes:
                if cliente.documento == c.documento:
                    raise Exception(
                        f'Cliente {cliente.nome} - {cliente.documento} já esta cadastrado no Banco {self.nome}')

        self._clientes.append(cliente)

    def inseir_conta(self, conta):
        if self._contas:

            if conta.agencia not in self._agencias:
                raise Exception(
                    f'AG: {conta.numero_conta} não faz parte do Banco {self.nome}')

            for c in self._contas:
                if c.numero_conta == conta.numero_conta:
                    raise Exception(
                        f'Conta: {conta.numero_conta} já faz parte do Banco {self.nome}')

        self._contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self._clientes:
            raise Exception(f'Cliente {cliente.nome} - doc {cliente.documento} não faz parte do banco {self.nome}')

        return True
