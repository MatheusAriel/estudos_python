import os
import shutil
import traceback

import requests
from bs4 import BeautifulSoup
import tqdm

try:

    termo_busca = input('Informe o termo a procurar: ')
    path = os.path.join("images/", termo_busca.replace(' ', '_'))
    if not os.path.exists(path):
        os.mkdir(path)

    url_base = 'https://www.zedge.net/find/{termo}'.format(termo=termo_busca.replace(' ', '%20'))
    response = requests.get(url_base)
    html = BeautifulSoup(response.text, 'html.parser')

    for div_images in html.select('#app-root'):
        images = div_images.find_all("a", href=lambda href: href and "https://www.zedge.net/wallpaper/" in href)

        for i, img in enumerate(images,1):

            response2 = requests.get(img['href'])
            html_page2 = BeautifulSoup(response2.text, 'html.parser')

            for value in html_page2.select('#app-root'):
                for src in value.find_all("img", src=lambda src: src and "https://fsb.zobj.net/crop.php?" in src):
                    r = requests.get(src.get('src'), stream=True)
                    if r.status_code == 200:
                        with open(f"{path}/{i}.jpg", 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)
except:
    traceback.print_exc()
    print('Erro')
