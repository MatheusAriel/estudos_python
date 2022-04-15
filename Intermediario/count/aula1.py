from itertools import count

contador = count(start=1, step=2.1)

print(next(contador))
print(next(contador))

"""
for x in contador:
    print(x)
"""

for x in contador:
    print(round(x, 2))
    if x >= 10:
        break

print()
contador2 = count(start=10, step=-1)

for x in contador2:
    print(x)
    if x >= 11 or x <= -10:
        break

print()

contador3 = count()
lista_nomes = ['Matheus', 'Camila', 'Ana', 'Maria', 'José']
lista = zip(contador3, lista_nomes)
print(list(lista))
