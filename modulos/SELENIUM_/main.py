"""
https://www.selenium.dev/pt-br/documentation

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

LOGIN = ''
SENHA = ''


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')

        # Com isso ele oculta do navegador que o chrome está sendo controlado por automa��o.
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)

        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_login(self):
        try:
            btn_login = self.chrome.find_element(by=By.LINK_TEXT, value='Sign in')
            btn_login.click()
        except Exception as err:
            print('Erro ao clicar em login: ', err)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def logar(self):
        try:
            input_login = self.chrome.find_element(By.ID, value='login_field')
            input_login.send_keys(LOGIN)

            password_login = self.chrome.find_element(By.ID, value='password')
            password_login.send_keys(SENHA)

            # btn_login = self.chrome.find_element(By.NAME, value='commit')
            # btn_login.click()

            password_login.send_keys(Keys.ENTER)

            # self.clicar_perfil()


        except Exception as err:
            print('Erro ao logar: ', err)

    def clicar_perfil(self):
        try:

            perfil = self.chrome.find_element(By.CSS_SELECTOR,
                                              value=r"body > div.position-relative.js-header-wrapper > header > div."
                                                    "Header-item.position-relative.mr-0.d-none.d-md-flex")
            perfil.click()
        except Exception as err:
            print('Erro ao clicar no perfil: ', err)

    def clicar_logout(self):
        try:
            logout = self.chrome.find_element(By.CSS_SELECTOR,
                                              value="body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button")
            logout.click()
        except Exception as err:
            print('Erro ao clicar em logout: ', err)

    def verificar_usuario(self, usuario):
        profile_link_html = self.chrome.find_element(By.CLASS_NAME, value='user-profile-link').get_attribute(
            'innerHTML')

        # assert usuario in profile_link_html
        if usuario in profile_link_html:
            self.clicar_logout()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    # sleep(1)
    # chrome.clica_login()
    # sleep(2)
    # chrome.logar()
    # chrome.clicar_perfil()
    # sleep(1)
    # chrome.verificar_usuario('MatheusAriel')

    sleep(1)
    #chrome.sair()
    # while True:
    #     chrome = ChromeAuto()
    #     chrome.acessa('https://google.com.br')
    #     sleep(60)
    #     chrome.sair()
