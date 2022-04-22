class Pessoa:
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

        var = 'Valor do init'

    def falar(self, msg=None):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já esta falando')
            return

        print(f'{self.nome} esta falando', msg if msg is not None else '')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando nada para parar de falar')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, comida=None):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} esta comendo', comida if comida is not None else '')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo nada para parar de comer')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
