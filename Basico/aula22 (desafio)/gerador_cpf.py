from random import randint

numero = str(randint(100000000, 999999999))
cpf_sem_digitos = numero

reversed = 10
total = 0
for index in range(19):
    if index > 9:
        index -= 9

    total += int(cpf_sem_digitos[index]) * reversed

    reversed -= 1
    if reversed < 2:
        reversed = 11

        total = 11 - (total % 11)
        d = 0 if total > 9 else total

        cpf_sem_digitos += str(d)
        total = 0

cpfComMascara = '{}.{}.{}-{}'.format(cpf_sem_digitos[:3],
                                     cpf_sem_digitos[3:6],
                                     cpf_sem_digitos[6:9],
                                     cpf_sem_digitos[9:])

print(f'CPF SEM MÁSCARA: {cpf_sem_digitos}')
print(f'CPF COM MÁSCARA: {cpfComMascara}')
