"""
    EM PYTHON TUDO É UM OBJETO: incluindo classes
    METACLASSES são as "classes" que criam classes.
    Type é uma metaclasse
"""

from classes2 import *

a = A()
b = B()
c = C()

print(b.att_classe)

print()
print(c.att_classe)
print()


class Pai:
    nome = 'TESTE PAI Z'


Z = type(
    # nome classe
    'Z',

    # herda de quem?
    (Pai,),

    # namespace tudo da classe (meotodos, atributos, etc)
    {
        'atributo': 'Atributo da classe Z'
    }
)
z1 = Z()
print(z1.atributo)
print(z1.nome)
