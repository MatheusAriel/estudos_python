from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        Conta.verificar_valor_numerico(valor)

        if (self.saldo + self.limite) < valor:
            raise Exception('Saldo insuficiente')
        self.saldo -= valor
        self.detalhar_conta()
