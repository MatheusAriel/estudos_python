from cep import *
from time import perf_counter
from tqdm import tqdm
import json

while True:
    try:
        vezes = int(input('Informe quantas requisições você deseja ? '))
        if vezes <= 0:
            break

        with open('enderecos.json', 'a+') as file:
            for i in tqdm(range(vezes)):
                try:
                    endereco = Cep.gerar_endereco()
                    cep = Cep(endereco['cep'], ApiCep.AWESOME)

                    if not cep.buscar_cep() is None:
                        # mostra todos os metodos e atributos da classe cep
                        # print(dir(cep))

                        json.dump(endereco, file, ensure_ascii=False)
                        file.write(',\n')
                except:
                    print('Erro')


    except:
        print('informe um número válido')
