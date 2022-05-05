import requests
from bs4 import BeautifulSoup

print('Noticias página inicial\n\n')
url = 'https://www.saocarlosagora.com.br/'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for noticia in html.select('.linkNoticia.comImgMenor'):
    # titulo = noticia.select_one('.imgNoicia').get('title')
    # ou
    titulo = noticia.select_one('.titulos h3')
    tema = noticia.select_one('.titulos small')
    data = noticia.find_all('small', class_=False, id=False)[0]
    # OU
    #    data = noticia.select('small', class_=False, id=False)[1]

    print('*' * 100)
    print(f'Título:\t{titulo.text}')
    print(f'Data:\t{data.text}')
    print(f'Tema:\t{tema.text}')
    print('*' * 100, '\n\n')


i=1
for i in range(100):
    print(i)