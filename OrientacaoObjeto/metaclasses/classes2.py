class Meta(type):

    def __new__(mcs, name, bases, name_space):
        if name == 'A':
            return type.__new__(mcs, name, bases, name_space)

        if 'att_classe' in name_space:
            print(f'{name} tentou sobreescrever o atributo att_classe...excluindo...\n')
            del name_space['att_classe']

        return type.__new__(mcs, name, bases, name_space)


class A(metaclass=Meta):
    att_classe = 'Valor A'


class B(A):
    att_classe = 'Valor B'


class C(B):
    att_classe = 'Valor C'
