import math

PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica_lista(lista, valor=1):
    r = valor
    for i in lista:
        r *= valor
    return r


# print('Módulo executando\n')

# retorna o nome do modulo, apenas se ele esta sendo chamado em algum outro lugar, se n sera o main mesmo
print(__name__)

print('\n\n')

# só sera executado aqui, e nao sera executado quando importado
if __name__ == '__main__':
    lista = [1, 2, 3, 45, 6, 7, 8, 9]
    print(dobra_lista(lista))
    print()
    print(multiplica_lista(lista, 3))
    print()
    print(PI)

