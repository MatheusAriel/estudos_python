from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: str, numero_conta: str, saldo: float):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    @staticmethod
    def verificar_valor_numerico(valor) -> bool:
        if not isinstance(valor, (int, float)):
            raise Exception('Valor precisa ser númerico')

        return True

    def detalhar_conta(self):
        print('\n********************************')
        print(f'Agência: {self.agencia}', end=' - ')
        print(f'Conta: {self.numero_conta}')
        print(f'Saldo R${self.saldo}')
        total = self.saldo
        if hasattr(self, 'limite'):
            total += self.limite
            print(f'Limite R${self.limite}')

        print(f'Saldo Total: R${total}')
        print('********************************\n')

    @saldo.setter
    def saldo(self, saldo: float):
        self.verificar_valor_numerico(saldo)
        self._saldo = saldo
        self.detalhar_conta()

    def depositar(self, valor: float):
        self.verificar_valor_numerico(valor)
        if valor > 0:
            self._saldo += valor
            self.detalhar_conta()
        else:
            raise Exception('Deposite um valor maior que 0')

    @abstractmethod
    def sacar(self, valor: float):
        pass
