import os
import utils
from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')

while True:
    caminho_procura = input('Informe o caminho: ').lower()
    termo_procura = input('Informe o termo de procura: ')
    caminho_procura = r'%s' % caminho_procura

    i = 0
    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        # print(f'raiz {raiz}')
        # print('*' * 100)
        # print(f'diretorios {diretorios}')
        # print('*' * 100)
        # print(f'arquivos {arquivos}')
        for arquivo in arquivos:
            if termo_procura.upper() in arquivo.upper():

                try:
                    i += 1
                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                    tamanho_arquivo = os.path.getsize(caminho_completo)
                    # print(arquivo, nome_arquivo, extensao_arquivo, tamanho_arquivo, sep=' | ')

                    data_modificacao = os.path.getmtime(caminho_completo)
                    data_modificacao = datetime.fromtimestamp(data_modificacao)

                    data_cricao = os.path.getctime(caminho_completo)
                    data_cricao = datetime.fromtimestamp(data_cricao)

                    print()
                    print('-=-' * 100)
                    print(f'Encontrei o arquivo: {arquivo}')
                    print(f'Caminho: {caminho_completo}')
                    print(f'Nome: {nome_arquivo}')
                    print(f'Extensão: {extensao_arquivo}')
                    print(f'Tamanho: {tamanho_arquivo}')
                    print(f'Tamanho Formatado: {utils.formatar_tamanho(tamanho_arquivo)}')
                    print('Data de criação do arquivo:', data_cricao.strftime('%A, %d de %B de %Y %H:%M:%S'))
                    print('Data da última modificacação no arquivo:', data_modificacao.strftime('%A, %d de %B de %Y %H:%M:%S'))
                    print('-=-' * 100)
                except PermissionError as error:
                    print(f'Sem permissão - Erro: {error}')
                except FileNotFoundError as error:
                    print(f'Arquivo não encontrado - Erro: {error}')
                except Exception as error:
                    print(f'Erro desconhecido - Erro {error}')

    print(f'{i} arquivo(s) encontrados com o termo "{termo_procura}"\n')
