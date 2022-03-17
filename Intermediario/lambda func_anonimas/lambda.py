def funcao(p1, p2):
    return p1 * p2


result = funcao(2, 3)
print(result)

print('\n')

result2 = lambda p1, p2: p1 * p2
print(result2(2, 10))

print('\n\n')

listaProdutos = [
    ['P1', 97],
    ['P2', 59],
    ['P3', 41],
    ['P5', 85],
    ['P4', 11]
]

"""
def ordenacaoPreco(item):
    return item[1]
"""

# listaProdutos.sort(key=ordenacaoPreco)

print(sorted(listaProdutos, key=lambda i: i[1]))
print(listaProdutos)

print('*******')

listaProdutos.sort(key=lambda i: i[1])
print(listaProdutos)
