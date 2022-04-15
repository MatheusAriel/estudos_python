from itertools import combinations, permutations, product

pessoas = ['Matheus', 'Lucas', 'Jandrei', 'Eduardo', 'Fernando', 'Airton', 'Gabriela']

for duplas_nao_repetidas in combinations(pessoas, 2):
    print(duplas_nao_repetidas)

print()
for duplas_repetidas in permutations(pessoas, 2):
    print(duplas_repetidas)

print()
for repetidos in product(pessoas, repeat=2):
    print(repetidos)
