from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite: float = 100):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite: float):
        self.verificar_valor_numerico(limite)
        self._limite = limite
        self.detalhar_conta()

    def sacar(self, valor: float) -> None:
        Conta.verificar_valor_numerico(valor)
        if (self.saldo + self.limite) < valor:
            raise Exception('Saldo insuficiente')
        self.saldo -= valor
        print(f'Valor Sacado: R${valor}', end='\n********************\n')
