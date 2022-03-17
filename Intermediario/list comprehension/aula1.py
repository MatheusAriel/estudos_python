l1 = list(range(1, 11))

print(l1)

ex1 = [v for v in l1]
print(ex1, type(ex1))

print()
ex2 = [v * 10 for v in l1]
print(ex2)

print()
ex3 = [v * i for v, i in enumerate(l1, 1)]
print(ex3)

print()
ex4 = [(v1, v2) for v1 in l1 for v2 in range(3)]
print(ex4)

print()
l2 = ['Luiz', 'Matheus', 'Camila', 'Saulo']
ex4 = [v.replace('a', '@').replace('z', 's').upper() for v in l2]
print(ex4)

print()
tupla = (
    ('Chave', 'Valor'),
    ('Chave2', 'Valor2'),
    ('Chave3', 'Valor3'),
)

print(tupla)
ex5 = [(y, x) for x, y in tupla]
print(ex5, type(ex5))

print()
l3 = list(range(100))
print(l3)
ex6 = [v for v in l3 if v % 2 == 0 if v % 8 == 0]
print(ex6)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else -1 for v in l3]
print(ex7)

