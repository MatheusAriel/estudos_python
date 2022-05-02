from datetime import datetime
from locale import setlocale, LC_ALL
import calendar

while True:
    try:
        setlocale(LC_ALL, '')

        dia = input('Informe o dia: ')
        mes = input('Informe o mês: ')
        ano = input('Informe o ano: ')

        data = datetime.strptime(f'{dia}/{mes}/{ano}', '%d/%m/%Y')
        # print(data)

        formatacao1 = data.strftime('%A, %d de %B de %Y')
        print(formatacao1)

        print(f'Último dia do mês de {data.strftime("%m/%Y")} é dia {calendar.mdays[int(data.strftime("%m"))]}')
    except:
        print('erro')
