from abc import ABC, abstractclassmethod


class A(ABC):

    @abstractclassmethod
    def falar(cls):
        pass


class B(A):

    def falar(self, msg):
        print('Classe B falando', msg)
