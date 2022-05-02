import traceback


class TaErradoError(Exception):
    pass


class ExceptPersonalizadaError(Exception):
    def __init__(self, message='', code=None, nome=None):
        self.code = code
        self.nome = nome
        msg = f"Está errado =( (código do erro {code}, Nome erro {nome})"
        super(ExceptPersonalizadaError, self).__init__(message or msg)


def testar():
    raise TaErradoError('Está Errado =(')


def testar2():
    raise ExceptPersonalizadaError('', 250, 'fora do ar')


# raise ExceptPersonalizadaError('Vish, errou')


try:
    testar()
except TaErradoError as erro:
    print(f'Erro: {erro}')

try:
    testar2()
except ExceptPersonalizadaError as erro:
    print(f'Erro: {erro}')
    print(f'Code: {erro.code}')
    print(f'Nome erro: {erro.nome}')
    print(f'Exceção do tipo {erro.__class__.__name__}')
    print('\n\n')
    traceback.print_exc()
