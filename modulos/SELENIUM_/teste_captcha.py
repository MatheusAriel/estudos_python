from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pathlib import Path
import traceback
import os
import twocaptcha
from time import sleep

ROOT_FOLDER = Path(__file__).parent.parent.parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for op in options:
            chrome_options.add_argument(op)

    chrome_service = Service(executable_path=CHROME_DRIVER_PATH)

    return webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )


if __name__ == '__main__':
    try:

        # options = ('--headless',)
        ops = ''  # ('--disable-gpu', '--no-sandbox')
        chrome = make_chrome_browser(*ops)

        # chrome.quit()

        chrome.get('https://g1.globo.com/')
        # sleep(1)
        #
        # botao_atualizar = chrome.find_element(By.ID, 'btnAtualizar')
        # botao_atualizar.click()
        # captch_img = chrome.find_element(By.CSS_SELECTOR,
        #                                  '[aria-label="Será necessário digitar o código da imagem, há um link abaixo para ouvi-lo"]')
        # captch_img.screenshot('capctha.png')

        # api_key = os.getenv('APIKEY_2CAPTCHA', '246fa67628d09580ac9395c6e0db9a94')
        # solver = twocaptcha.TwoCaptcha(api_key)
        # result = solver.normal('captcha.png')

        myElem = WebDriverWait(chrome, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'glb-topo')))
        print("carregou pagina")
        noticia = chrome.find_element(By.CLASS_NAME, 'feed-media-wrapper')
        noticia.click()
        myElem = WebDriverWait(chrome, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'glb-topo')))
        print('Carregou noticia')

    except TimeoutException:
        print("Time out n achou glb-topo || feed-media-wrapper apos 3 segundos na pagina")
    except:
        print(traceback.print_exc())
