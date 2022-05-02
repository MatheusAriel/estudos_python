from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ano_atual = int(dt.strftime('%Y'))
dia_atual = int(dt.strftime('%d'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')

# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1, formatacao2)
print(dia_atual, mes_atual, mdays[mes_atual], ano_atual)

print(f'Dia Atual {dia_atual}')
print(f'Mês Atual {mes_atual}')
print(f'Ultimo dia do Mês Atual {mdays[mes_atual]}')
print(f'Ano Atual {ano_atual}')



