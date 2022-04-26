"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __init__(self):
        print('CLASSE A __INIT__')

    def __new__(cls, *args, **kwargs):
        print('CLASSE A __NEW__ PRIMEIRO METODO EXECUTADO DE UMA CLASSE')
        # return super().__new__(cls)
        # ou
        cls.nome = 'Matheus Ariel'

        def haha(*args, **kwargs):
            return 'HAHAHAHHA'

        cls.risada = haha
        return object.__new__(cls)



a = A()
print(a.nome)
print(a.risada())
