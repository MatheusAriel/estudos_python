# kwargs são argumentos nomeados

def func_kwargs(**kwargs):
    print(f'Esses foram os parametrosd vindos para a func: {kwargs} e vieram um total de: {len(kwargs)} parametros')
    print()
    print(kwargs.get('nome'))
    print(kwargs.get('nacionalidade'))
    print(kwargs.get('idade'))
    print(kwargs.get('lista_linguagens'))
    print(kwargs.get('peso'))



func_kwargs(nome='Matheus', nacionalidade='Brasileira', idade=28,
            lista_linguagens=('java', 'javascript', 'php', 'python'), sexo='Masculino')
