# -*- encoding: utf-8 -*-

import requests
import os
import shutil
from tqdm import tqdm


def get_wallpaper(busca: str, qtd_busca: int = 10) -> dict:
    try:
        url = "https://api-gateway.zedge.net/"

        payload = {
            "query": "query search($input: SearchAsUgcInput!) {     searchAsUgc(input: $input){ ...browseContentItems"
                     "Resource}}fragment browseContentItemsResource on BrowseContentItems {page total items {... on "
                     "BrowseWallpaper {id contentType title tags imageUrl placeholderUrl licensed}... on "
                     "BrowseRingtone {id contentType title tags imageUrl placeholderUrl licensed meta "
                     "{durationMs previewUrl gradientStart gradientEnd}}}}",
            "variables": {"input": {"contentType": "WALLPAPER", "keyword": f"{busca}", "page": 1, "size": qtd_busca}}}

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            raise Exception(f'Erro na conexão: {response.status_code}')



    except:
        raise Exception('Erro na conexão')
    else:
        return response.json()


def tratar_retorno(json: dict, caminho: str) -> None:
    for i, images in enumerate(tqdm(json['data']['searchAsUgc'].get('items')), 1):
        url_img = images['imageUrl']
        if 'https://fsb.zobj.net/crop.php?' in url_img:
            r = requests.get(url_img, stream=True)
            if r.status_code == 200:
                with open(f"{caminho}/{i}.jpg", 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            del r


try:
    termo_busca = input('Informe o termo a procurar: ')
    qtd = int(input('Informe a quantidade: '))

    retorno = get_wallpaper(termo_busca, qtd)

    if not retorno['data']['searchAsUgc'].get('items'):
        raise Exception("Nenhum resultado encontrado")

    path = os.path.join("download/", termo_busca.replace(' ', '_'))
    if not os.path.exists(path):
        os.mkdir(path)

    tratar_retorno(retorno, path)

except (Exception, ValueError, ConnectionError) as err:
    print(f'Erro: {err}')
else:
    print('Finalizado com suceso!')
