from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

        var = 'vari[avel do init(construtor)'

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

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
