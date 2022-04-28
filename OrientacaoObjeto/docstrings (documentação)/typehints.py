"""Descrição ráida e simples sobre a classe

ele não faz nada, mas é ó um exemplo para você
typing = https://docs.python.org/3/library/typing.html

"""

variavel: str = 'Varivale qualquer'
x: int = 10
y: float = 20.2
z: bool = False


def funcao(p1: float, p2: int, p3: bool, p4: str, p5: dict, p6: tuple):
    return p1, p2, p3, p4, p5, p6


var = funcao(10.2, 1, False, 'Teste', {'nome': 'Matheys'}, ('chave', 'valor'))


# como indicar qual tipo de dado (qndo é um tipo só) q a função retorna
def funcao2(p1: int, p2: int) -> int:
    return p1 + p2


print(funcao2(10, 10))

from typing import Union


# como indicar qual tipo de dado (qndo pode ser mais de um tipo) q a função retorna
def funcao3() -> Union[list, dict]:
    return []


print(funcao3())
