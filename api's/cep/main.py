from cep import *
from time import time

while True:
    vezes = input('Informe quantas requisições você deseja ? ')
    try:
        vezes = int(vezes)
        if vezes > 0:
            break
    except:
        print('informe um número válido')

i = 1
start_time = time()

while i <= vezes:
    endereco = Cep.gerar_endereco()
    # print(endereco['cep'])
    c1 = Cep(endereco['cep'], ApiCep.AWESOME)
    print('\t', f'Req: {i} - {c1.buscar_cep()}')
    print('\n')
    i += 1

end_time = time()
time_process = (end_time - start_time)
print(f'Tempo total de processo {vezes} requisições: {time_process:.2f} segundos')
