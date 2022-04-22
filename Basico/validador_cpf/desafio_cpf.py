try:
    cpfDigitado = input('Digite seu cpf: ')
    cpfDigitado = cpfDigitado.replace('.','')
    cpfSplit = cpfDigitado.split('-')
    cpf = cpfSplit[0]
    i = sum = sum2 = 0

    for n in range(10, 1, -1):
        sum += int(cpf[i]) * n
        i = i+1

    conta1 = (11 - (sum % 11))
    digito1 = 0 if conta1 > 9 else conta1

    cpf = cpf + cpfSplit[1][0]
    i = 0
    for n in range(11, 1, -1):
        sum2 += int(cpf[i]) * n
        i = i+1

    conta2 = (11 - (sum2 % 11))
    digito2 = 0 if conta2 > 9 else conta2

    if cpfDigitado.replace('-','') == (cpfSplit[0]+str(digito1)+ str(digito2)):
        print('CPF válido')
    else:
        print('CPF inválido')
except:
    print('Erro no sistema')




