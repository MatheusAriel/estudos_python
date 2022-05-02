from datetime import datetime
from locale import setlocale, LC_ALL
import calendar

setlocale(LC_ALL, '')
# setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
print(dt)

print()
# dia da semana, dia de mes de ano atual
formatacao1 = dt.strftime('%A, %d de %B de %Y')
print(formatacao1)

print()
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao2)

print()
mes_atual = int(dt.strftime('%m'))
ano_atual = int(dt.strftime('%Y'))
dia_atual = int(dt.strftime('%d'))
ultimo_dia_mes = calendar.mdays[mes_atual]

print(f'Dia Atual {dia_atual}')
print(f'Mês Atual {mes_atual}')
print(f'Ultimo dia do Mês Atual {ultimo_dia_mes}')
print(f'Ano Atual {ano_atual}')
