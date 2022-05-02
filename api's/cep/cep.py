import requests
from time import time
from random import choice
from enum import Enum
import traceback


class ApiCep(Enum):
    AWESOME = 'https://cep.awesomeapi.com.br/json/{CEP}'
    VIA_CEP = 'https://viacep.com.br/ws/{CEP}/json'


class Cep:
    def __init__(self, cep: str, api=ApiCep.AWESOME):
        self._cep = cep
        self.api = api

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
        def wrapper(*args):
            start_time = time()
            f = func(*args)
            end_time = time()
            time_process = (end_time - start_time)
            print(f'Tempo de processo do {func.__name__}: {time_process:.2f} segundos')
            return f

        return wrapper

    @_calcular_tempo_request
    def buscar_cep(self):
        try:
            if not isinstance(self.api, ApiCep):
                raise ValueError("API inválida")

            link = self.api.value.replace('{CEP}', self.cep)
            # link = f'https://cep.awesomeapi.com.br/json/{self.cep}'
            # link = f'https://viacep.com.br/ws/{self.cep}/json'
            request = requests.get(link)
            if request.status_code != 200:
                raise ConnectionError(f'Erro ao gerar endereço')

            request = request.json()

        except (ConnectionError, requests.exceptions.ConnectionError) as erro:
            print(f'Erro na conexão - {erro}')
        except (ValueError, TypeError, Exception) as erro:
            print(f'Erro: {erro}')
        else:
            return request

    @staticmethod
    @_calcular_tempo_request
    def gerar_endereco():
        try:
            lista_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
                             'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF']

            # link = f"https://geradornv.com.br/wp-json/api/cep/random-by-states?state={choice(lista_estados)}"

            link = "https://www.invertexto.com/ajax/gerar-cep.php"
            request = requests.post(link)

            if request.status_code != 200:
                raise ConnectionError(f'Erro ao gerar endereço')

            if 'message' in request and request['message'] == 'error':
                raise ConnectionError(f'Erro ao gerar endereço')

        except (ConnectionError, requests.exceptions.ConnectionError) as erro:
            print(f'Erro ao gerar ENDEREÇO - {erro}')
        except Exception as erro:
            print(f'Erro ao gerar ENDEREÇO - {erro}')
            traceback.print_exc()
        else:
            return request.json()


if __name__ == '__main__':
    endereco = Cep.gerar_endereco()
    print(endereco['cep'])

    # print('COM AWESOME API: ')
    # cep = Cep(endereco['cep'])
    # print('\t', cep.buscar_cep())
    #
    # print('\n\n', '*' * 50, '\n\n')
    #
    # endereco = Cep.gerar_endereco()
    # print('COM VIA CEP API: ')
    # cep = Cep(endereco['cep'], ApiCep.VIA_CEP)
    # print('\t', cep.buscar_cep())
