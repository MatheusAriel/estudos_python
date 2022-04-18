from dados import produtos, pessoas, lista

# usando list comprehension
"""lista_pares = [x for x in lista if x % 2 == 0]
print(lista_pares)"""

lista_pares = list(filter(lambda x: x % 2 == 0, lista))
print(lista_pares)

print()

# produtos com preços maiores q 10 reais
lista_produtos_caros = filter(lambda p: p['preço'] >= 50, produtos)

print('Lista de produtos caros')
for p in lista_produtos_caros:
    print(p)

print()


def filtra_produto_preco(produto, valor):
    if (produto['preço'] >= valor):
        return True


print()
lista_produtos_caros2 = filter(lambda p: filtra_produto_preco(p, 50), produtos)
print('Lista de produtos caros2')
for p in lista_produtos_caros2:
    print(p)

print()
pessoas_maiores_idade = filter(lambda p: p['idade'] >= 18, pessoas)
print(list(pessoas_maiores_idade))

print()
def filtra_menores_idade(pessoa):
    if pessoa['idade'] < 18:
        return True

lista_menores_idade = filter(filtra_menores_idade, pessoas)
print(list(lista_menores_idade))