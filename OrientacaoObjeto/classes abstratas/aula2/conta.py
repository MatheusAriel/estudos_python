from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @staticmethod
    def verificar_valor_numerico(valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor precisa ser númerico')

        return True

    @saldo.setter
    def saldo(self, saldo):
        self.verificar_valor_numerico(saldo)
        self._saldo = saldo

    def depositar(self, valor):
        self.verificar_valor_numerico(valor)
        self._saldo += valor
        self.detalhar_conta()

    def detalhar_conta(self):
        print(f'Agência {self.agencia}', end=' - ')
        print(f'Conta {self.conta}')
        print(f'Saldo R${self.saldo}', end='\n*********************\n')

    @abstractclassmethod
    def sacar(self, valor):
        pass
