tupla = ('Nova York', 'Boston', 'Londres', 'Chicago', 'São Paulo', 'Rio de Janeiro', 'Santos')
print(tupla[-1], type(tupla), tupla[2:5])

print('\n')

tupla2 = (1, 2, 3, 4, 5)
print(tupla2, type(tupla2))

tupla3 = 10, 20, 30, 40, 50,

tupla5 = tupla2 + tupla3
print(tupla5)

print('\n')

v1, v2, *_, ultimo = tupla5

print(v1, v2, _, ultimo)

print('\n')
print(tupla2 * 3)
print('\n')

print(tupla2)
lista = list(tupla2)
lista[-1] = 'Z'
print(lista, type(lista))
tuplaz = tuple(lista)
print(tuplaz, type(tuplaz))
