try:
    lista = []
    dict = {}
    print(dict[2])
    print(lista[1])
    print(a)
except NameError as er:
    print(f'Erro -  {er}')
except (IndexError, KeyError) as er:
    print('Erro de índice ou chave')
except Exception as er:
    print('Ops, Ocorreu um erro inesperado')

print('\nContinua a executar o código\n\n')

try:
    dict = {}
    print(1 / 0)
except NameError as er:
    print(f'Erro -  {er}')
except (IndexError, KeyError) as er:
    print('Erro de índice ou chave')
except Exception as er:
    print('Ops, Ocorreu um erro inesperado')
else:
    print('Código executado com sucesso sem erros')
    print(dict)
finally:
    print('Idependentemente de sucesso ou erro, serei executado')

print('\n\n\n\n')

try:
    a = 1 / 0
except NameError as er:
    print(f'Erro -  {er}')
except (IndexError, KeyError) as er:
    print('Erro de índice ou chave')
except Exception as er:
    print('Ops, Ocorreu um erro inesperado')
else:
    pass
finally:
    a = None

print(a)
