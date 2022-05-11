import pyautogui
import pyperclip
import pandas as pd
from time import sleep

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=403, y=269, clicks=2)
pyautogui.click(button='right')
pyautogui.click(x=488, y=639)
sleep(3)

# pyautogui.hotkey('ctrl', 't')

# sleep(5)
# print(pyautogui.position())

tabela = pd.read_excel(r'C:\Users\mathe\Downloads\Vendas - Dez.xlsx')

soma_valor_final = tabela['Valor Final'].sum()
soma_quantidade = tabela['Quantidade'].sum()
# print(soma_valor_final, soma_quantidade)


pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(x=141, y=174)
sleep(1)
pyautogui.write('matheusariel@hotmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatórios de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f"""
prezados bom dia


O faturamento ontem foi de: R${soma_valor_final:,.2f}
A quantidade total de produtos foi de: {soma_quantidade:,}

obg, pyautogui
"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
