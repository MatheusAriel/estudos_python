from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]

print(lista)
print(list(nova_lista))


def dobra_valor(produto):
    produto['preço'] = produto['preço'] * 2
    return produto


print()
produtos_precos_novos = map(dobra_valor, produtos)

for produto in produtos_precos_novos:
    print(produto)

print('\n\n')


# idade_dobradas = map(lambda p:p['idade']*2, pessoas)

def dobra_idade(pessoa):
    pessoa['idade_dobrada'] = pessoa['idade'] * 2
    return pessoa

p = map(dobra_idade, pessoas)

for x in p:
    print(x)
