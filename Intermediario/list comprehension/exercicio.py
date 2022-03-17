string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
comp = [(i, i + n) for i in range(0, len(string), n)]
print(comp)

list = [string[i: i + n] for i in range(0, len(string), n)]
print(list)

new_string = '.'.join(list)
print(new_string)

print()
nome = 'Matheus'
dois_em_dois = [
    nome[indice:indice + 2]
    for indice in range(0, len(nome), 2)
]

print(dois_em_dois)
