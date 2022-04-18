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


def multiplica_idade(pessoa, multiplicacao):
    pessoa[f'idade_multiplicacao_por_{multiplicacao}'] = pessoa['idade'] * multiplicacao
    return pessoa


p = map(lambda p: multiplica_idade(p, 20), pessoas)

for x in p:
    print(x)
