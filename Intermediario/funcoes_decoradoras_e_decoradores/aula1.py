



def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave

@master
def falar_oi():
    print('Oi')

#aqui a funcao falar_oi esta decorada
#falar_oi = master(falar_oi)
falar_oi()


print('\n##############\n')

def master2(funcao):
    print('MASTER2()')
    def slave(*args, **kwargs):
        print('SLAVE()')
        funcao(*args,**kwargs)
    return slave

@master2
def outra_func(msg):
    print('OUTRA_FUNC()')
    print(msg)


print()
outra_func('Olá sou Matheus')