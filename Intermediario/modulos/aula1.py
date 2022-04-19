'''
#assim importa o modulo sys inteiro
import sys
print(sys.platform)
'''

'''
#ou assim importa tudo, mas n eh recomendavel
from sys import *
print(platform)
'''

from sys import platform as so

print(so)

print()

from random import randint, random

print(randint(1, 10))
print(random())

"""
instalar : pip install nome_modulo
desinstalar: pip uninstall nome_modulo
"""
