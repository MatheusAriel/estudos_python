class Caneta:
    def __init__(self, marca, cor):
        self.__marca = marca
        self.__cor = cor

    @property
    def marca(self):
        return self.__marca.title()

    @property
    def cor(self):
        return self.__cor.title()

    def escrever(self):
        print(f'A caneta {self.marca} está escrevendo em {self.cor}..')
