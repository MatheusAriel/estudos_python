import requests
from bs4 import BeautifulSoup
from time import perf_counter

()

try:
    nro_paginas = int(input("Informe a quantidade de páginas q deseja: "))
    url = 'https://www.saocarlosagora.com.br/ultimas-noticias/p/{}/'
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    i = 1
    start = perf_counter()
    nro_noticias = 0
    while i <= nro_paginas:
        url = url.format(i)

        for noticia in html.select('.linkNoticia'):
            titulo = noticia.select_one('.titulos.ultimas-noticias h3')
            data = noticia.find_all('small', attrs={'class': '.listaData'}, class_=False, id=False)[0]
            hora = noticia.find_all('small', attrs={'class': '.listaData'}, class_=False, id=False)[1]
            tipo = noticia.find_all('small', attrs={'class': '.listaData'}, class_=False, id=False)[2]
            descricao = noticia.select_one('.titulos.ultimas-noticias h5')

            nro_noticias += 1
            print('*' * 100)
            print(f'Data:\t{data.text} {hora.text}')
            print(f'Título:\t{titulo.text}')
            print(f'Tipo:\t{tipo.text}')
            print(f'Descrição: {descricao.text.replace("&nbsp;;", "")}')
            print('*' * 100, '\n\n')
        i += 1

    end = perf_counter()

    print(f'Total de páginas:{i-1} - noticias: {nro_noticias} - duração: {(end - start):.2f} segundos')
except:
    print('Erro')
