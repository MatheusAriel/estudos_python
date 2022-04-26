from conta import Conta


class ContaPoupanca(Conta):

    def sacar(self, valor):
        Conta.verificar_valor_numerico(valor)

        if self.saldo < valor:
            raise Exception('Saldo insuficiente')
        self.saldo -= valor
        self.detalhar_conta()
