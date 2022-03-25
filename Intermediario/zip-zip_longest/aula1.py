from itertools import zip_longest, count

cidades = ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte', 'Brasília', 'Campinas']
estados = ['SP', 'RJ', 'PR', 'MG']
indices = count()

print('Zip:')
cidades_estados = zip(estados, cidades)
# print(list(cidades_estados))
print(dict(cidades_estados))

print()
print('Zip Longest')
longest_cidades_estados = zip_longest(indices, estados, cidades, fillvalue='UF')
# print(list(longest_cidades_estados))

zip_cidades_estados = zip(indices, estados, cidades)

for indice, estado, cidade in zip_cidades_estados:
    print(indice, estado, cidade)
