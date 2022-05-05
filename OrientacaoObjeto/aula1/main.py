from pessoa import Pessoa

p1 = Pessoa('Matheus', 28)

print(dir(p1))

p1.falar()
p1.falar()
p1.comer('Pizza')
p1.comer('Arroz')
p1.parar_comer()
p1.parar_comer()
p1.comer('Arroz')
p1.parar_falar()
p1.parar_falar()
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.falar('OB')

print()
print(p1.get_ano_nascimento())

print(Pessoa.ano_atual)