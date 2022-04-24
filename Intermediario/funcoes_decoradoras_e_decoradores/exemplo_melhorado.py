import requests
from time import time

"""https://www.youtube.com/watch?v=P0aW1czXHio"""


def calcular_tempo(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        time_process = (end_time - start_time)
        print(*args)
        print(f'Tempo de processo do script: {time_process:.2f} segundos')

    return wrapper


@calcular_tempo
def pegar_cotacao_dolar(msg):
    link = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    valor = requisicao['USDBRL']['bid']
    valor = float(valor)
    print(f"R$ {valor:.2f}")


pegar_cotacao_dolar('Essa é a cotação do dólar')
