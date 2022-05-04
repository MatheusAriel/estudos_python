import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)

# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')
# print(html, type(html))


for pergunta in html.select('.s-post-summary.js-post-summary'):
    titulo = pergunta.select_one('.s-link')
    # pegar o texto do html
    # print(titulo.text)

    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')

    print('*' * 100)
    print(f'Título:\t{titulo.text}')
    print(f'Data:\t{data.text}')
    print(f'Votos:\t{votos.text}')
    print('*' * 100, '\n\n')
