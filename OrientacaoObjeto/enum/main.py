from enum import Enum, auto


class Direcoes(Enum):
    # esquerda = 0
    # direita = 1
    # cima = 2
    # baixo = 3

    esquerda = auto()
    direita = auto()
    cima = auto()
    baixo = auto()


def move(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError("Direcão inválida")

    # print(direcao.__dict__)
    # print(direcao.value)
    return f'Movendo {direcao.name}'


if __name__ == '__main__':
    print(move(Direcoes.direita))
    print(move(Direcoes.esquerda))
    print(move(Direcoes.cima))

    print('*' * 155)

    for direcao in Direcoes:
        print(direcao, direcao.value, direcao.name)
