"""
POLIMOSFISMO é o princípio que permite que classes derivadas (classes filhas) de uma mesma
super classe (classe pai) tenham métodos iguais (de MESMA ASSINATURA) mas comportamentos diferentes

MESMA ASSINATURA  = mesma quantidade e tipo de parametros
"""


from classes import *

b = B()
c = C()

b.falar('Assunto')
print(b.calcular(10))

print()
c.falar('Outro Assunto')
print(c.calcular(10))

