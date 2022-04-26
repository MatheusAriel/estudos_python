"""
https://rszalski.github.io/magicmethods/
"""


class A:

    def __setattr__(self, key, value):
        if key == 'sobrenome':
            self.__dict__[key] = f'Voce não pode setar um {key} nesse objeto'
        else:
            self.__dict__[key] = value


a = A()
a.nome = 'Matheus Souza'
print(a.nome)

print()
a.sobrenome = 'Souza'
print(a.sobrenome)
