from itertools import groupby, tee

alunos = [
    {'nome': 'Matheus', 'nota': 'A'},
    {'nome': 'Nestor', 'nota': 'C'},
    {'nome': 'Camila', 'nota': 'A'},
    {'nome': 'Claudio', 'nota': 'B'},
    {'nome': 'Gilberto', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'D'},
    {'nome': 'Carlos', 'nota': 'B'},
    {'nome': 'Lucas', 'nota': 'D'},
]

order = lambda i: i['nota']

alunos.sort(key=order)
for aluno in alunos:
    print(aluno)

print()
alunos_agrupados = groupby(alunos, order)
for agrupamento, valores_agrupados in alunos_agrupados:
    v1, v2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')
    print(f'\tQuantidade de alunos: {len(list(v1))}')

    for aluno in v2:
        print(f'\t\taluno: {aluno}')
    print()


