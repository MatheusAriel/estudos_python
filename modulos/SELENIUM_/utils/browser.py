"""
https://developers.google.com/web/updates/2017/04/headless-chrome
https://copilot.github.com/
https://www.selenium.dev/pt-br/documentation/webdriver/waits/
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path

# caminho raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent.parent
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
    # options = ('--headless',)
    ops = ('--disable-gpu', '--no-sandbox')
    chrome = make_chrome_browser(*ops)

    chrome.get('https://www.google.com')

    input_search = chrome.find_element(by=By.NAME, value='q')
    input_search.send_keys('palmeiras')
    input_search.send_keys(Keys.ENTER)

    # chrome.quit()
