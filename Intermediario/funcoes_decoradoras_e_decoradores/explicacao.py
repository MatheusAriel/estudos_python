"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.
"""


def decorar(funcao):
    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('############')
        funcao()
        print('############')

    return funcao_decorada


@decorar
def printar():
    for i in range(3):
        print(i)


#nova_printar = decorar(printar)
#nova_printar()
printar()
# Saída:
# ############
# 0
# 1
# 2
# ############
# 
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Python faz é X = decorador(X).

print('\n\n\n')

def decorador1(sua_funcao, *args, **kwargs):
    print('O decorador1 foi executado', end='\r\n\r\n')

    def funcao_que_vai_substituir_a_sua(*args, **kwargs):
        # só pra salpicar algo nos args (só funciona com strings e só nos args)
        print('Adicionando decorador1 nos args')
        manipulando_args = [f'{v} - decorador1' for v in args]
        return sua_funcao(*manipulando_args, **kwargs)

    return funcao_que_vai_substituir_a_sua


def decorador2(sua_funcao, *args, **kwargs):
    print('O decorador2 foi executado', end='\r\n\r\n')

    def funcao_que_vai_substituir_a_sua(*args, **kwargs):
        # só pra salpicar algo nos args (só funciona com strings e só nos args)
        print('Adicionando decorador2 nos args')
        manipulando_args = [f'{v} - decorador2' for v in args]
        print('Args agora:', *manipulando_args)
        return sua_funcao(*manipulando_args, **kwargs)

    return funcao_que_vai_substituir_a_sua


@decorador2  # decorador2 segundo
@decorador1  # decorador1 primeiro
def a_minha_funcao_1(msg):
    return msg


@decorador1  # decorador1 segundo
@decorador2  # decorador2 primeiro
def a_minha_funcao_2(msg):
    return msg


print('RESULTADO COM a_minha_funcao_1:', a_minha_funcao_1('oi'))
print()
print('RESULTADO COM a_minha_funcao_2:', a_minha_funcao_2('Hello'))