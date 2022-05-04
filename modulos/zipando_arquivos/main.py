from zipfile import ZipFile
import os
import string
import random


letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-+=/¨":?|'

for i in range(10):
    with open(f'arquivos/teste{i}.txt', 'w') as file:
        senha = "".join(random.choices((letras + digitos + caracteres), k=500))
        file.write(f'Senha: {senha}')
    i += 1

caminho = r'arquivos'
print('\n Compactando os arquivos em zip\n', '*' * 99)
with ZipFile('arquivos.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
    print('Compactado com sucesso\n\n')

print('\n Mostrando os aquivos do zip\n', '*' * 99)
with ZipFile('arquivos.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

print('\n Descompatando\n', '*' * 99)
with ZipFile('arquivos.zip', 'r') as zip:
    zip.extractall('descompactado')
    print('Descompactado com sucesso !')
