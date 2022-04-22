"""
import vendas.calculos_precos

preco = 50.50
preco_com_aumento = vendas.calculos_precos.aumento(preco, porcentagem=10)
print(preco_com_aumento)

"""

# OU
"""
from vendas import calculos_precos

preco = 50.50
preco_com_aumento = calculos_precos.aumento(preco, porcentagem=10)
print(preco_com_aumento)
"""

# OU
from vendas.calculos_precos import aumento, reducao
#from vendas.formata.preco import real
import vendas.formata.preco as formata

preco = 50.50
preco_com_aumento = aumento(preco, porcentagem=10, formata=True)
preco_com_reducao = reducao(preco, porcentagem=10, formata=False)

print(preco_com_aumento, formata.real(preco_com_reducao))
