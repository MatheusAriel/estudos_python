from contextlib import contextmanager


@contextmanager
def abrir_arquivo(arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(arquivo, modo)
        #ao inves de usar return usar yield
        yield arquivo
    except Exception as err:
        print(f'Erro: {err}')
    finally:
        print('fechando arquivo')
        arquivo.close()


with abrir_arquivo('abc3.txt', 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    #arquivo.nada()
    arquivo.write('Linha 4\n')

