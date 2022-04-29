from dataclasses import dataclass


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
    p1 = Pessoa('Matheus', 'Souza', 30)
    # print(p1)
    # print(p1.nome)
    # print(p1.idade)
    # print(p1.nome_completo)

    p2 = Pessoa('Marcio', 'Mendes', 30)
    p3 = Pessoa('Alberto', 'silva', 40)
    p4 = Pessoa('Zalberto', 'anjo', 50)

    lista_pessoas = [p1, p2, p3, p4]
    #print(f'lista de pessoas ordernadas nome: order True {sorted(lista_pessoas)}')

    print(
        f'lista de pessoas ordernadas sobrenome: order True '
        f'{sorted(lista_pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=False)}')

    #print(p2)
    #print(p1 == p2)
