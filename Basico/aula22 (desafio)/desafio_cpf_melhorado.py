while True:
    try:
        cpf = input('Digite seu cpf: ')
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

        if (len(cpf) < 11):
            raise Exception('CPF inváldo')

        cpf_sem_digitos = cpf[:-2]

        reversed = 10
        total = 0
        for index in range(19):

            # verifica até os 9 primeiros digitos
            if index > 9:
                index -= 9

            total += int(cpf_sem_digitos[index]) * reversed

            # print(cpf[index],reversed, index)

            reversed -= 1
            if reversed < 2:
                reversed = 11

                total = 11 - (total % 11)
                d = 0 if total > 9 else total

                cpf_sem_digitos += str(d)
                total = 0

        if cpf == cpf_sem_digitos and not (cpf_sem_digitos == str(cpf_sem_digitos[0]) * len(cpf)):
            print('CPF válido')
        else:
            raise Exception('CPF inváldo')

    except Exception as e:
        print(str(e))
