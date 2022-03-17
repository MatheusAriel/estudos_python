def func1(func, *args):
    # print(type(func2()))
    return func2(args[0], args[1])


def func2(v1, v2):
    return v1 + v2


result = func1(func2, 1, 2)

print(result)

print('\n\n')


def bem_vindo(nome):
    print(f'Seja bem vindo {nome}')


def saudacao(saudacao, nome):
    print(saudacao, nome)


def main(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


main(bem_vindo, 'Matheus')
main(saudacao, nome='Matheus', saudacao='Olá')
