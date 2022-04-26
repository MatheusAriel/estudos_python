"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste

    def __init__(self):
        # print('CLASSE A __INIT__')
        pass

    def __call__(self, *args, **kwargs):
        print(f'args: {args}', end='\n\n')
        print(f'kwargs: {kwargs}')

        resultado = [x + x for x in args]
        return resultado


    def falar_oi(self):
        print('oi')


a = A()
b = A()
c = A()

print()
print(a == b)
print(b == c)

print()
print(id(a), id(b), id(c))

print()
var = a(1, 2, 3, 4, 5, nome='Matheus')
print(var)
a.falar_oi()
