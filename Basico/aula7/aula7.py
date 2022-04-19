nome = "Matheus Ariel"
idade = 28
altura = 1.77
permissao = idade > 18
peso = 95
imc = peso/(altura**2)
data_nascimento = 2022-idade

#print(nome,'tem', idade,'anos', 'e seu imc =', imc)
print(f'{nome} tem {idade} anos e seu imc {imc:.2f}')

print('{0} tem {1} anos e seu imc {2:.2f}, esse é o {0}'.format(nome, idade, imc))

print('Nascido em {dn}, {n} tem {i} anos, pesa {p}kg e seu imc {im:.2f}, esse é o {n}'.format(n=nome, i=idade, im=imc, p=peso, dn=data_nascimento))

