from dataclasses import dataclass, field, asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)
    idade: int = field(default=20)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(f'Parametro nome precisa ser uma string e não uma {type(self.nome)} em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
    p1 = Pessoa('Jorge', 'Camargo')
    print(p1)

    #p2 = Pessoa(2, 'Nandes', 23)

    print(asdict(p1))
    print(astuple(p1))
