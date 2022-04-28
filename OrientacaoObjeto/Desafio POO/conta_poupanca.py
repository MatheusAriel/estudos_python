from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
        self.detalhar_conta()

    def sacar(self, valor: float):
        Conta.verificar_valor_numerico(valor)
        if (self.saldo) < valor:
            raise Exception('Saldo insuficiente')
        self.saldo -= valor
        print(f'Valor Sacado: R${valor}', end='\n********************\n')
