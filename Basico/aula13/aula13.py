num1 = 1

print(f'{num1:0<4}')

print(f'{num1:0^4}')

print(f'{num1:0>4}')


num2 = 120
print(f'{num2:.2f}')
print(f'{num2:0>10.2f}')


nome = 'NOME DE TESTE'
print(f'\n\n{nome:*^100}')
qtd_caracteres = 100 - len(nome)
#nome_formatado = '{n:#^qtd}'.format(n=nome, qtd=qtd_caracteres)
#print(nome_formatado)


texto = 'Esse é um texto de exemplo'
print('\n\n',texto[5])
print(texto[0::2])

url = 'www.text.com/'
print('\n\n',url[:-1])
print(url[0:3])
print(url[:-5])
print(url[8:])
for letra in url:
    print(letra)