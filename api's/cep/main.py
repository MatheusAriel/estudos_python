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
    c1 = Cep(endereco['cep'], ApiCep.AWESOME)
    print('\t', f'Req: {i} - {c1.buscar_cep()}')
    print('\n')
    i += 1

end_time = perf_counter()
time_process = (end_time - start_time)
print(f'Tempo total de processo {vezes} requisições: {time_process:.2f} segundos')
