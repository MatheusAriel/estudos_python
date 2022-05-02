from calendar import monthrange
from datetime import datetime

ano = 2022
mes = 2

# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(ano, mes))

# Saída - (1, 28)
# O 1 significa que é uma terça feira
# O 28 significa que este é o último dia do mês


dia_semana, ultimo_dia = monthrange(ano, mes)
print(ultimo_dia)  # ultimo dia do mes

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(ano, mes)[1] for mes in range(1, 13)
]

print(ultimos_dias_de_meses_do_ano_atual)
