from endereco import Endereco


class Cliente:
    def __init__(self, nome, sexo):
        self._nome = nome
        self._sexo = sexo
        self.enderecos = []

    def __del__(self):
        print(f'{self.nome} foi apagado da memória')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.upper()

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        if (sexo not in ['M', 'F']):
            sexo = 'O'
        self._sexo = sexo.upper()

    def inserir_endereco(self, cep, numero):
        self.enderecos.append(Endereco(cep, numero))

    def listar_enderecos(selfs):
        if selfs.enderecos:
            print(f'Lista de endereços de {selfs.nome}: ')
            for endereco in selfs.enderecos:
                print(f'\tCEP: {endereco.cep} - Complemento: {endereco.complemento}')
        else:
            print(f'{selfs.nome} não posssui endereços cadastrados')
