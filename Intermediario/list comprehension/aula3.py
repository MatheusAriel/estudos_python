"""https://www.youtube.com/watch?v=M2zL6LnQwkw&t"""

lista_precos = [1000, 1500, 2000, 300, 250, 150, 890, 3500]
print(lista_precos)
print()
# dobrar os valores da lista

# modo convencional

print('Lista com valores dobrados:')
lista_precos_dobrados = []
for preco in lista_precos:
    lista_precos_dobrados.append(preco * 2)

print(lista_precos_dobrados)

# modo com List Comprehension

lista_precos_dobrados_2 = [preco * 2 for preco in lista_precos]
print(lista_precos_dobrados_2)

print('\n#####\n')
print('Lista de valores com impostos:')

# se valor for mais q mil, adicionar 50% sobre ele

# modo convencional

lista_impostos = []
for preco in lista_precos:
    valor = preco
    if (preco > 1000):
        valor = valor + (valor * 0.5)

    lista_impostos.append(valor)

print(lista_impostos)

# modo com List Comprehension

lista_impostos_2 = [preco + preco * 0.5 if preco > 1000 else preco for preco in lista_precos]
print(lista_impostos_2)
