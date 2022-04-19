string = 'Abacaxi; Morango; Uva; Maçã'
listFrutas = string.split('; ')  # transforma em lista uma string por determinada regra
print(listFrutas)

print('\n\n')

frase = 'O Brasil é pentacampeão do mundo, sendo o maior de todo'
fraseList = frase.split(' ')
for palavra in fraseList:
    print(f'A palavra {palavra} apareceu {frase.count(palavra)}x na frase')

print('\n\n')

lista = ['Sony', 'Lenovo', 'dELL', 'HP']
stringMarcas = ' | '.join(lista)  # transforma lista em string separando por determianda regra
print(stringMarcas.upper())

print('\n\n')

for index, value in enumerate(fraseList):  # enumerar elementos de uma lista
    # print(index, value)
    print(f'A palavra {value} esta no indice {index} da frase')

print('\n\n')

list = [
    [0, 'Matheus'],
    [1, 'Carlos'],
    [2, 'Pedro']
]

listNomes = ['Matheus', 'Carlos', 'Pedro']
v1, v2, v3 = listNomes
print(v3)

for index, value in enumerate(listNomes):
    print(index, value)

print('\n\n')

listTurmas = [
    'TURMA1', ['1º', '2º', '4ª'],
    'TURMA2', ['3º', '5º', '6ª'],
]

for index, value in enumerate(listTurmas):
    print(index, value)

print('\n\n')

list1 = [
    ['Edu', 'Cézar', 'Júlio'],
    ['Miguel', 'Ricardo', 'Anderson'],
    ['Ana', 'Helena', 'Maria']
]

for index, value in enumerate(list1, 100):
    print(index, value)
    for index2, value2 in enumerate(value):
        print(value2)

print('\n\n')

arrays = ['Luiz', 'Gilberto', 'Ana', 1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]

# n1, n2, n3,*arrays2, ultimoElemento = arrays
*arrays2, n1, n2, n3 = arrays

print(n1)
