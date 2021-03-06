import requests
from time import perf_counter
from enum import Enum


class ApiCep(Enum):
    AWESOME = 'https://cep.awesomeapi.com.br/json/{}'
    VIA_CEP = 'https://viacep.com.br/ws/{}/json'


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
            start_time = perf_counter()
            f = func(*args)
            end_time = perf_counter()
            time_process = (end_time - start_time)
            print(f'Tempo de processo do {func.__name__}: {time_process:.3f} segundos')
            return f

        return wrapper

    # @_calcular_tempo_request
    def buscar_cep(self):
        try:
            if not isinstance(self.api, ApiCep):
                raise ValueError("API inválida")

            url = self.api.value.format(self.cep)
            request = requests.get(url=url, timeout=10)

            if request.status_code != 200:
                raise ConnectionError(f'Erro ao gerar endereço - CODE {request.status_code} | MSG {request.json()}')

            return request.json()

        except (ConnectionError, requests.exceptions.ConnectionError) as erro:
            print(f'Erro na conexão - {erro}')
        except (ValueError, TypeError, Exception) as erro:
            print(f'Erro: {erro}')

    @staticmethod
    # @_calcular_tempo_request
    def gerar_endereco():
        try:
            '''lista_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
                             'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF']
            link = f"https://geradornv.com.br/wp-json/api/cep/random-by-states?state={choice(lista_estados)}" '''

            url = "https://www.invertexto.com/ajax/gerar-cep.php"
            request = requests.post(url=url, timeout=10)

            if request.status_code != 200:
                raise ConnectionError(f'Erro ao gerar endereço CODE {request.status_code} | MSG {request.json()}')

            if 'message' in request and request['message'] == 'error':
                raise ConnectionError(f'Erro ao gerar endereço')

        except (ConnectionError, requests.exceptions.ConnectionError, Exception) as erro:
            print(f'Erro ao gerar endereço - {erro}')
        else:
            return request.json()


if __name__ == '__main__':
    cep = Cep('14815100', ApiCep.AWESOME)

    print(cep.buscar_cep())
