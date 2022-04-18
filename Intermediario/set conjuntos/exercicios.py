"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 2],
]


def verifica_repeticao_lista(lista):
    set_verificados = set()
    for index, value in enumerate(lista, 1):
        set_verificados.add(value)
        if len(set_verificados) != index:
            return value
    return -1


for lista in lista_de_listas_de_inteiros:
    print(lista)
    result = verifica_repeticao_lista(lista)
    print(f'Não há numeros repetidos na lista' if result < 0 else f'O primeiro numero repetido da lista é: {result}')
    print()

print('\n\n\t\t****************************************************************************************')


def solucao2(param_lista_inteiros):
    set_checados = set()
    duplicado = -1
    for numero in param_lista_inteiros:
        if numero in set_checados:
            duplicado = numero
            break
        set_checados.add(numero)
    return duplicado


for l in lista_de_listas_de_inteiros:
    solucao2(l)
    print(l)
    result = solucao2(l)
    print(f'Não há numeros repetidos na lista' if result < 0 else f'O primeiro numero repetido da lista é: {result}')
    print()

"""
ola
"""