import copy

dicionario = {
    'chave1': 'valor',
}
dicionario['chave2'] = 200
print(dicionario, type(dicionario), dicionario['chave1'])

print('\n\n')
d2 = dict(chave1='valor2', chave2='valor2')
print(d2, type(d2), d2['chave1'])
msg = 'existe chave 3' if 'chave3' in d2 else 'Não existe chave3'
print(msg)

print('\n\n')
d3 = {'chave': 'valor', 'chave': 'valor real pois é o ultimo'}
print(d3)

print('\n\n')
d4 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: True}
print(d4)

print('\n\n')
d5 = {
    'string': 'ABCD',
    'Inteiros': 1234,
    'Tupla1': (1, 2, 3, 4),
    (1, 2, 3, 4): 'Tupla2',
    'decimal': 12.4,
}
print(d5, d5[(1, 2, 3, 4)])

print(d5.get('chavenaoexistente'))
msg = 'Não existe [chavenaoexistente]' if d5.get('chavenaoexistente') is None else 'Existe [chavenaoexistente]'
print(msg)

d5['string'] = 'Outro valor string'
d5['outra_string'] = 'ytiuoeep'

print(d5)

d5.update({'boleanos': True, 'nome': 'Matheus'})
print(d5)

del d5['nome'], d5['outra_string']
print(d5)

print('carlos' in d5)
print('Inteiros' in d5.keys())

print('algumvalor' in d5.values())
print(1234 in d5.values())

print('\n\n')
d6 = {
    'chave1': 'A',
    'chave2': 'B',
    'chave3': 'C',
    'chave4': 'D',
}

print(len(d6))

for index in d6:
    print(index)

for value in d6.values():
    print(value)

for k in d6.items():
    print(k, type(k))

for i, v in d6.items():
    print(i, v)

print('\n\n')

clientes = {
    'cliente1': {
        'nome': 'Matheus',
        'sobrenome': 'Souza',
        'idade': 28
    },
    'cliente2': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
        'idade': 36
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira',
        'idade': 66
    },
}

for clientes_i, clientes_v in clientes.items():
    print(f'Exibindo: {clientes_i}')
    for dados_i, dados_v in clientes_v.items():
        print(f'\t{dados_i} =  {dados_v}')
    print('\n')

print('\n\n')

d8 = {1: 'a', 2: 'b', 3: 'c', 'lista': ['Matheus', 'Souza']}
v1 = d8
print(d8, v1)
v1[1] = 'z'
print(d8, v1)

v1 = d8.copy()
v1[1] = 'ZWY'
print(v1, v1['lista'][0])
print(d8)
v1['lista'][0] = 'Carlos'

print(d8, v1)

v2 = copy.deepcopy(d8)
v2['lista'][0] = 'Matheus'
print(d8, v2)

print('\n\n')
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
    ['c4', 4]
]

dic = dict(lista)
print(dic)
dic.pop('c1')
print(dic)
dic.popitem()#elimina o ultimo elemento do dicionario
print(dic)

dic.update(d2)
print(dic)



