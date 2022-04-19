#             0               1         2           3
array = ['Playstation', 'Microsoft', 'Nintendo', 'Sega'];
#            -4            -3          -2          -1


array.append('Neo Geo')  # append insere no final da lista

array.insert(0, 'Capcom')  # insere onde quer na lista

print(array)
print(array[0])
print(array[-1])
print(array[:2])
print(array[-3:])
print('******************\n\n')

l1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
l2 = [4, 5, 6]
print()
print(l1 + l2)
l1.extend(l2)
l1.append('BANANA')
print(l1)
l1.pop()  # remove o ultimo elemento da lista
print(l1)

l1.append('Maçã')
print(l1)
del (l1[-1])
print(l1)

del (l1[3:5])
print(l1)

print(max(l1))
print(min(l1))

l3 = list(range(1, 11))
print(l3)

del (l3[2:5])
print(l3)

l4 = ['String', True, 10, -90.5]

for x in l4:
    print(f'O tipo do elemento é {type(x)} e seu valor é: {x}')

jogo1 = 'GTA'
jogo2 = 'Bully'
jogo3 = 'Max Payne'

listJogos = [jogo1, jogo2, jogo3]

print(listJogos)
print()
# o 3 recebera do terceiro pra frente
lista = [*range(1,11)]
v1, v2, *v3 = lista

print(v1, v2, v3)
