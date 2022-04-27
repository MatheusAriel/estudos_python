"""Descrição ráida e simples

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ultricies dui eu enim efficitur cursus. Cras sit amet
fermentum dui. Pellentesque vitae posuere felis. Sed convallis dui sit amet mattis egestas. Etiam ut eleifend orci. Ut
efficitur dolor ligula, ac volutpat turpis pulvinar quis. Etiam nec elementum nunc. Nunc ligula tellus, finibus a
rutrum ut, feugiat ac lectus. Nullam cursus efficitur est, aliquam semper ligula sodales quis. Nullam a auctor purus.
Sed bibendum vulputate tristique. Proin urna mauris, dignissim ut tempor non, maximus nec mi.

REFERENTE AO MÓDULO ISSO TUDO

"""

variavel = 'valor'


def somar(x, y):
    """soma x + y"""
    return x + y


def multiplicar(x, y, z=None):
    """multiplica x,y,z

    multiplica x,y,z. O programador pode omitir a variavel z caso não tenha necessidade em usá-la
    """
    if z:
        result = x * y * z
    else:
        result = x * y
    return result


var1 = 10
var2 = 30
var3 = 40
