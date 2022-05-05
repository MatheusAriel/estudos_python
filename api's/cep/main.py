from cep import *
from time import perf_counter
from tqdm import tqdm

while True:
    try:
        vezes = int(input('Informe quantas requisições você deseja ? '))
        if vezes > 0:
            break
    except:
        print('informe um número válido')

start_time = perf_counter()

for i in tqdm(range(vezes)):
    endereco = Cep.gerar_endereco()
    cep = Cep(endereco['cep'], ApiCep.AWESOME)
    cep.buscar_cep()
    # print(dir(cep))#mostra todos os metodos e atributos da classe cep
    # print('\t', f'Req: {i} - {cep.buscar_cep()}')

end_time = perf_counter()
print(f'Tempo total de processo {vezes} requisições: {(end_time - start_time):.2f} segundos usando a api {ApiCep.AWESOME.name}')
