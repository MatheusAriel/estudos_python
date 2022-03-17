def func(p1, p2, p3=None, p4=None):
    print(p1, p2, p3, p4)


func(1, 2, 45, 'A')

print('\n\n')


# quando não sei quantos parametros vou precisar pra função
def func2(*args):
    # args[0]= 'MAtheus'
    # #dara erro pois nao pode alterar valor de tupla. e args eh uma tupla, caso queira alterar valores, fazer cast para list

    args2 = list(args)

    print(len(args))
    print(args)
    print(args[-1])
    print(type(args))

    for value, index in enumerate(args):
        print(value, index)

    args2[0] = "Lucas"
    print(args2)
    print(type(args2))


func2(1, 200, 458, 4, 5)

print('\n\n')

# o * desempacota a lista
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(*lista1, sep='|')

print('\n\n')

listaNomes = ['Matheus', 'Alberto']
func2(*lista1, *listaNomes)

print('\n\n')


# kwars são argumentos nomeados
def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'])
    print(kwargs['nacionalidade'])
    # print(kwargs['idade'])

    print('*******************')
    # melhor usar assim. pois nao dara erro caso n exista o parametro no kwargs, só retornará None
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    print(nome, idade)


func3(*lista1, nome='Matheus', nacionalidade='Brasileira')

print('\n\n')

variavel = 'Brasil'


def func4():
    #variavel = 'Chile'
    #print(variavel)
    global variavel
    variavel = 'Argentina'
    print(variavel)

print(variavel)
func4()
print(variavel)
