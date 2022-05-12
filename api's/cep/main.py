from cep import *
from time import perf_counter
from tqdm import tqdm
import json

while True:
    try:
        vezes = int(input('Informe quantas requisições você deseja ? '))
        if vezes > 0:
            break
    except:
        print('informe um número válido')

start_time = perf_counter()

with open('enderecos.txt', 'w') as file:
    for i in (range(vezes)):
        endereco = Cep.gerar_endereco()
        print(endereco)
        #cep = Cep(endereco['cep'], ApiCep.AWESOME)
        #cep.buscar_cep()

        # mostra todos os metodos e atributos da classe cep
        # print(dir(cep))

        json.dump(endereco, file)
        file.write('\n')

end_time = perf_counter()
print(
    f'Tempo total de processo {vezes} requisições: {(end_time - start_time):.2f} segundos usando a api {ApiCep.AWESOME.name}')
