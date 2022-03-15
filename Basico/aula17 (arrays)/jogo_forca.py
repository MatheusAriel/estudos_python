palavra_secreta = input('Digite uma palavra mágica para o jogador: ').upper()
digitadas = digitadas_erradas = []

changes = 2
while True:
    if(changes<=0):
        print('Voce perdeu')
        break


    letra = input('Digite uma letra: ').upper()
    if len(letra)>1:
        print('Digite apenas uma letra')
        continue

    if letra in digitadas_erradas:
        print(f'Você já tentou essa letra: {letra}, tente outra')
        continue

    if letra not in palavra_secreta:
        changes-=1

    if letra in palavra_secreta:
        print(f'Acertou a letra "{letra}"')
        digitadas.append(letra)
    else:
        print(f'Errou a letra "{letra}"')
        print(f'Você ainda tem {changes} change')
        if letra not in digitadas:
            digitadas_erradas.append(letra)

    aux = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            aux += letra_secreta
        else:
            aux+= '*'

    print(aux)

    if(aux == palavra_secreta):
        print('Prabéns')
        break