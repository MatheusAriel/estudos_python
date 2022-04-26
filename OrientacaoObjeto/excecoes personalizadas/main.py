class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Errado =(')


try:
    testar()
except TaErradoError as err:
    print(f'Errado : {err}')
