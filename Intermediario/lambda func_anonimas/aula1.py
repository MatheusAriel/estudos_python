"""https://www.youtube.com/watch?v=xmMXULd0dxc"""

preco = 1000


def calcular_imposto(valor, percentual=0.3):
    return valor * percentual


print('Sem lambda: ')
print(calcular_imposto(preco, 0.3))

# calcular_imposto_2 = lambda valor, percentual: valor * percentual
# antes dos : eh parametro e depois dos : e o return
calcular_imposto_2 = lambda x, y: x * y
print('Com lambda')
print(calcular_imposto_2(preco, 0.3))

print()
lista_precos = [1000, 100, 500, 10, 25]
impostos = list(map(lambda x: x * 0.3, lista_precos))
print(impostos)

impostos2 = list(map(calcular_imposto, lista_precos))
print(impostos2)
