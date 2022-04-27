"""
namespace é tudo o que está dentro da classe antes da criação do objeto, ou seja, métodos, atributos de classe,
etc...
"""


class Meta(type):

    def __new__(mcs, name, bases, name_space):
        if name == 'A':
            return type.__new__(mcs, name, bases, name_space)

        if 'b_falar' not in name_space:
            print(f'Oi, vc precisa implementar o metodo b_fala em {name}')
        else:
            # como saber se aquilo é uma funcao ou nao
            if not callable(name_space['b_falar']):
                print(f'b_falar precisa ser um método e não um atributo em {name}')

        return type.__new__(mcs, name, bases, name_space)


class A(metaclass=Meta):
    def a_falar(self):
        return self.b_falar()


class B(A):
    teste = 'VALOR QUALQUER'
    b_falar = 'não quero criar o metodo b_falar'

    def metodo_qualquer(self, msg):
        print(msg)

    def b_falar(self):
        print('B falando...')
