import sys
import os

# python .\main.py -d

argumentos = sys.argv
print('Argumentos: ', argumentos)

qtd_argumentos = len(argumentos)
if qtd_argumentos <= 1:
    print('Faltando argumentos')
    print('-a para listar todos os arquivos dessa pasta', sep='\t')
    print('-d para listar todos os diretorios dessa pasta', sep='\t')
    sys.exit()

so_arquivos = False
so_diretorios = False

if '-a' in argumentos:
    so_arquivos = True

if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)
