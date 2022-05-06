import os
import shutil

import requests
from bs4 import BeautifulSoup

termo_busca = input('Informe o termo a procurar: ')
qtd_images = input('Informe a quantidade de imagens: ')

path = os.path.join("download/", termo_busca.replace(' ', '_'))
if not os.path.exists(path):
    os.mkdir(path)

url_base = "http://books.toscrape.com/"
html_page = requests.get(url_base)

soup = BeautifulSoup(html_page.content, 'html.parser')

warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling

images = book_container.findAll('img')
example = images[0]
print(example)

url_ext = example.attrs['src']

full_url = url_base + url_ext

r = requests.get(full_url, stream=True)
if r.status_code == 200:
    with open(f"{path}/book1.jpg", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
