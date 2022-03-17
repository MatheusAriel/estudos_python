def funcao1(nome='', saudacao='Boa tarde'):
    if len(nome) > 1:
        # print(saudacao.upper(), nome.upper())
        return f'{saudacao}, {nome}'


print(funcao1('Matheus', 'Boa noite'))
print(funcao1('Jão'))
print(funcao1('Carla'))
print(funcao1('Ana', 'Bom dia'))
print(funcao1())

print('\n\n')


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


result = divisao(10, 2)
if result:
    print(result)
else:
    print('Conta inválida')

print('\n\n')


def func1(var):
    print(var)


def func2():
    return func1


var = func2()
var('TExto')
print(var)

print('\n\n')


def dumb():
    return 'Matheus', 'Daniel'


print(dumb()[0], type(dumb()))

print('\n\n')


def percentual(value, percent):
    return value + (value / 100 * percent)


print(percentual(100, 10))

print('\n\n')


def fb(var):
    if (var % 3 == 0 and var % 5 == 0):
        return 'FizzBuzz'
    if (var % 3 == 0):
        return 'Fizz'
    if (var % 5 == 0):
        return 'Buzz'

    return '#@&*+_!'


print(fb(107))
