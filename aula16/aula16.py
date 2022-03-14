lista = [1, 2, 3, 'A', 10.9, 'Carro']

print(lista[-1])#exibe o ultimo elemento da lista
for x in lista:
    #print('Lista:',x)
    print(f'Lista:{x}')

for n, letra in enumerate('Matheus Ariel'):
    print(n, letra)

print()


count = 2
for i in range(1,11):
    print(f'{count}*{i} = {count*i}')
