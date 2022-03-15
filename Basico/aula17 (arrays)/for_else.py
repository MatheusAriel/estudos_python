nomes = ['Matheus', 'lucas', 'Luiz', 'Gilberto', 'Fernando', 'João']

while True:
    letra = input('Com qual letra desja começar ? ').upper()
    if len(letra)==1:
        break


for n in nomes:
    if n.upper().startswith(letra): #verifica se a string começa com determinada letra
        print(f'Começa com {letra}', n)
        break
else:
    print(f'Não existe nenhum nome começado com {letra}')