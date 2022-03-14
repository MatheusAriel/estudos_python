num1 = (input('Digite um numero: '))

if (num1.isdigit()):
    if (int(num1) % 2 != 0):
        print(f'{num1} é ímpar')
    else:
        print(f'{num1} é par')
else:
    print('Informe um número inteiro valido')

hora = (input('\n\nDigite o horário (entre 0 e 23): '))
try:
    hora = int(hora)
    if (hora > 23 or hora < 0):
        print('Horário inválido')
    else:
        if (hora >= 0 and hora <= 11):
            print('Bom dia')
        elif (hora >= 12 and hora <= 17):
            print('Boa Tarde')
        else:
            print('Boa Noite')
except:
    print('Informe o horário em inteiro')

nome = input('\n\nInforme o seu nome: ')
if (len(nome) <= 4):
    print('Seu nome é curto')
elif (len(nome) >= 6):
    print('Seu nome é grande')
else:
    print('Seu nome é normal')
