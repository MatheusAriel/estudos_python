import random
import string

# Gera um número inteiro entra A e B
inteiro = random.randint(10, 20)
print(inteiro, '\n')

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(100, 1000, 10)  # começa em 100, até 999, pula de 10 em 10
print(inteiro, '\n')

# Gera um número de ponto flutuante entra A e B
flutuante = random.uniform(10, 20)
print(flutuante, '\n')

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()
print(flutuante, '\n')

lista_nomes = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista_nomes, 2)
print(sorteio, '\n')

sorteio = random.choices(lista_nomes, k=2)
print(sorteio, '\n')

sorteio = random.choice(lista_nomes)
print(sorteio, '\n')

# Embaralha a lista
random.shuffle(lista_nomes)
print(lista_nomes, '\n')


print('##################')

lista_numeros = range(25)
print(lista_numeros)
print(random.sample(lista_numeros,15))

