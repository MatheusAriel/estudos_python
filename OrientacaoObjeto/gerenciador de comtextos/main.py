"""
arquivo = open('abc.txt')
arquivo.write('alguma coisa\n')
arquivo.close()
"""

# isso é um gerenciador de contexto
with open('teste.txt', 'a+') as arquivo:
    arquivo.write('alguma coisa\n')


# criando meu gerenciador de contexto
class Arquivo:
    def __init__(self, arquivo, modo):
        print('init')
        self.arquivo = open(arquivo, modo)

    # durante o with
    def __enter__(self):
        print('enter')
        return self.arquivo

    # na saida do with
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit', end='\n*****\n')
        self.arquivo.close()

        # print(exc_type)
        # print(exc_val)
        # print(exc_tb)

        #depois de tratar as exceções
        return True


with Arquivo('abc2.txt', 'a+') as arquivo:
    arquivo.write('alguma coisa\n')
    arquivo.funcao_q_nao_existe()
