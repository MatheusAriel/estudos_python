import requests
from bs4 import BeautifulSoup
from time import perf_counter
import traceback
from tqdm import tqdm

try:
    nro_paginas = int(input("Informe a quantidade de páginas q deseja: "))
    url = 'https://www.saocarlosagora.com.br/ultimas-noticias/p/'


    nro_noticias = 0

    with open('noticias.txt', 'w') as file:
        start = perf_counter()

        for i in tqdm(range(nro_paginas)):
            url = url[0:53] + str(i+1)
            response = requests.get(url)
            html = BeautifulSoup(response.text, 'html.parser')

            for noticia in html.select('.linkNoticia'):
                titulo = noticia.select_one('.titulos.ultimas-noticias h3')
                data = noticia.find_all('small', attrs={'class': '.listaData'}, class_=False, id=False)[0]
                hora = noticia.find_all('small', attrs={'class': '.listaData'}, class_=False, id=False)[1]
                tipo = noticia.find_all('small', attrs={'class': '.listaData'}, class_=False, id=False)[2]
                descricao = noticia.select_one('.titulos.ultimas-noticias h5')
                link_noticia = noticia.select_one('.titulos.ultimas-noticias')

                nro_noticias += 1

                file.write('*' * 70)
                file.write(f'\nData:\t{data.text} | {hora.text}')
                file.write(f'\nTítulo:\t{titulo.text}')
                file.write(f'\nTipo:\t{tipo.text}')
                file.write(f'\nLink:\t{link_noticia["href"]}')
                file.write(f'\nDescrição:\t{descricao.text.replace("&nbsp;", "")}\n')

                """
                response2 = requests.get(link_noticia['href'])
                html2 = BeautifulSoup(response2.text, 'html.parser')
                for conteudo in html2.select('.grid_10.alpha.prefix_1.suffix_1'):
                    paragrafos = conteudo.find_all('p',class_=False, id=False)
                    for paragrafo in paragrafos:
                        print(paragrafo)
                        if '<p ppad="true"' in paragrafo:
                            print(paragrafo.text)
                    # print(paragrafos[0])
                    # print(paragrafos[0])

                    # print(paragrafo.text)
                """
                file.write('*' * 70)
                file.write('\n\n')

        end = perf_counter()
        msg = f'\nTotal de páginas: {i+1} - noticias: {nro_noticias} - duração: {(end - start):.2f} segundos'
        file.write(msg)
        print(msg)
except:
    print(traceback.print_exc())
    print('Erro')
