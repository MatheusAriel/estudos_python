class A:
    def falar(self):
        print(f'Falando... Estou em A')


class B(A):
    def falar(self):
        print(f'Falando... Estou em B')


class C(A):
    def falar(self):
        print(f'Falando... Estou em C')


class D(C, B):
    pass
