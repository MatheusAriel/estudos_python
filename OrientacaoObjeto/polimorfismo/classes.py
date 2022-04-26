from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def falar(self, msg):
        pass

    @abstractmethod
    def calcular(self, numero):
        pass


class B(A):
    def falar(self, msg):
        print(f'Classe B está falando {msg}')

    def calcular(self, numero):
        return 100 + numero


class C(A):
    def falar(self, msg):
        print(f'Classe C está falando {msg}')

    def calcular(self, numero):
        return 100 * numero
