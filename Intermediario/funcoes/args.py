# quando não sei quantos parametros vou precisar pra função, usa-se args

def func_args(*args):
    print(f'Vieram {len(args)} parametros e esses foram os parametros recebidos pela func {args}')


func_args('Matheus', 28, 1.77, {'carro': 'siena'}, 'Sexo')
