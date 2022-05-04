from cep import *
from time import perf_counter

while True:
    vezes = input('Informe quantas requisições você deseja ? ')
    try:
        vezes = int(vezes)
        if vezes > 0:
            break
    except:
        print('informe um número válido')

i = 1
start_time = perf_counter()

while i <= vezes:
    endereco = Cep.gerar_endereco()
    cep = Cep(endereco['cep'], ApiCep.AWESOME)
    cep.buscar_cep()
    # print(dir(cep))#mostra todos os metodos e atributos da classe cep
    print(f'Req: {i}\n')
    # print('\t', f'Req: {i} - {cep.buscar_cep()}')
    i += 1

end_time = perf_counter()
print(
    f'Tempo total de processo {vezes} requisições: {(end_time - start_time):.2f} segundos usando a api {ApiCep.AWESOME.name}')
