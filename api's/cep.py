import requests
import traceback
from time import time


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
            print(f'Tempo de processo do script: {time_process:.2f} segundos')
            return f

        return wrapper

    @_calcular_tempo_request
    def buscar_cep(self):
        try:
            self.cep = self._cep
            link = f'https://cep.awesomeapi.com.br/json/{self.cep}'
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


if __name__ == '__main__':
    c1 = Cep('00000000')
    print(c1.buscar_cep())
