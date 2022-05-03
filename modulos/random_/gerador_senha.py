import random
import string
import traceback

# Gera senha aleatória

while True:

    try:
        tamanho_senha = int(input('Informa o tamanho da sua senha: '))
        deseja_digitos = input('Deseja que sua senha possua dígitos? [Y-N]  ').upper()
        deseja_especiais = input('Deseja que sua senha possua caracteres especiais? [Y-N]  ').upper()

        if deseja_especiais and deseja_especiais not in ['Y', 'N']:
            raise Exception('Escolha uma opção válida')

        letras = string.ascii_letters
        digitos = string.digits
        caracteres = '!@#$%&*._-+=/¨":?|'

        geral = letras
        if deseja_digitos == 'Y':
            geral += digitos
        if deseja_especiais == 'Y':
            geral += caracteres

        senha = "".join(random.choices(geral, k=tamanho_senha))

        print(f'Sua senha é: {senha}')
    except ValueError:
        print('Erro: informa um número válido')
    except Exception as er:
        print(f'Erro: {er}')
