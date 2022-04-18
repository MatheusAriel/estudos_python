from dados import produtos, pessoas, lista
from functools import reduce

"""
acumula = 0
for x in lista:
    acumula += x
print(f'Somando todos os valores da lista: {acumula}')
"""

acumula = reduce(lambda acumulador, i: i + acumulador, lista, 0)
print(f'Somando todos os valores da lista: {acumula}')

print()
soma_valores_produtos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(f'Somando todos os valores dos produtos: R$ {soma_valores_produtos:.2f}')


print()
soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(f'A soma das idades das pessoas é: {soma_idades} e a média das idades é: {int(soma_idades / len(pessoas))} anos')
