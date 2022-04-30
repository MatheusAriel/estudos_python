import requests
from time import time
from random import choice


class Cep:
    def __init__(self, cep: str):
        self._cep = cep

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        if not isinstance(cep, str):
            raise TypeError(f'Cep precisa ser uma string')

        cep = cep.replace('-', '')
        if len(cep) != 8:
            raise ValueError(f'Cep inválido')

        self._cep = cep

    def _calcular_tempo_request(func):
        def wrapper(self):
            start_time = time()
            f = func(self)
            end_time = time()
            time_process = (end_time - start_time)
            print(f'Tempo de processo do {func.__name__}: {time_process:.2f} segundos')
            return f

        return wrapper

    @_calcular_tempo_request
    def buscar_cep(self):
        try:
            self.cep = self._cep
            link = f'https://cep.awesomeapi.com.br/json/{self.cep}'
            # link = f'https://viacep.com.br/ws/{self.cep}/json'
            request = requests.get(link)
            request = request.json()

            if 'status' in request and request['status'] != 200:
                raise ConnectionError(f'Status {request["status"]} - {request["message"]}')

        except (ConnectionError, requests.exceptions.ConnectionError) as erro:
            print(f'Erro na conexão - {erro}')
        except (ValueError, TypeError, Exception) as erro:
            print(f'Erro: {erro}')
        else:
            return request

    @staticmethod
    def gerar_endereco():
        try:
            estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
                       'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP',
                       'SE', 'TO', 'DF']
            link = f"https://geradornv.com.br/wp-json/api/cep/random-by-states?state={choice(estados)}"
            request = requests.get(link)
            request = request.json()

            if 'message' in request and request['message'] == 'error':
                raise ConnectionError(f'Erro ao gerar endereço')

        except (ConnectionError, requests.exceptions.ConnectionError) as erro:
            print(f'Erro ao gerar ENDEREÇO - {erro}')
        except Exception as erro:
            print(f'Erro ao gerar ENDEREÇO - {erro}')
        else:
            return request


if __name__ == '__main__':
    while True:
        endereco = Cep.gerar_endereco()
        # print(endereco)
        c1 = Cep(endereco['cep'])
        print(c1.buscar_cep())
