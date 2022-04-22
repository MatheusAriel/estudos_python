"""def lista_clientes(clientes_iteraveis, lista=[]):
    lista.extend(clientes_iteraveis)
    return lista"""


def lista_clientes(clientes_iteraveis, lista=None):
    if (lista is None):
        lista = []
    lista.extend(clientes_iteraveis)
    return lista


lista_clientes_1 = ['Fabrício']

clientes_1 = lista_clientes(['João', 'Maria', ' José', 'Carlos'], lista_clientes_1)
print(clientes_1)

clientes_2 = lista_clientes(['Marcos', 'Douglas', 'Lucas'])
print(clientes_2)

clientes_3 = lista_clientes(['Luiz'], lista_clientes_1)
print(clientes_3)

#print(clientes_1)
#print(clientes_2)
#print(clientes_3)
