class Endereco:
    def __init__(self, cep, complemento):
        self._cep = cep
        self.complemento = complemento

    def __del__(self):
        print(f'{self.cep} - {self.complemento} foi apagado da memória')

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep.replace(' ', '').replace('-', '')
