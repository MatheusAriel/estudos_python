"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __repr__(self):
        return f'classe A criada">'

    def __str__(self):
        return 'essa é a classe A criada para tal coisa'

    def __del__(self):
        print('Objeto coletado')

    def __len__(self):
        return 1001


a = A()
print(a)
print(f'Tamanho de a {len(a)}')
