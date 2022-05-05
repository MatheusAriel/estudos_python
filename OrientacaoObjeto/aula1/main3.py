from pessoa import Pessoa

p1 = Pessoa.por_ano_nascimento('Matheus', 1993)
print(dir(p1))

print(p1.__dict__)
print(p1.nome, p1.idade)
print(Pessoa.gerar_id())
print(p1.gerar_id())
