import re, random


def limpa_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def mascara_cnpj(cnpj):
    return '{}.{}.{}/{}-{}'.format(cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])


def calcula_digito(cnpj, i=5):
    soma_numeros = 0
    for n in cnpj:
        if i >= 2:
            # print(f'i = {i}  | digito = {n}')
            soma_numeros = soma_numeros + (i * int(n))
            i = i - 1
            if i == 1:
                i = 9
    soma_numeros
    calc = 11 - (soma_numeros % 11)
    return calc if calc <= 9 else 0


def verifica_sequencial(cnpj):
    if (cnpj[0] * len(cnpj)) == cnpj:
        raise 'CNPJ Sequencial'
    return True


def validar_cnpj(cnpj):
    try:
        cnpjOriginal = limpa_cnpj(cnpj)
        cnpj = cnpjOriginal[0:-2]

        verifica_sequencial(cnpj)
        digito = calcula_digito(cnpj, i=5)
        cnpj += str(digito)

        digito = calcula_digito(cnpj, i=6)
        cnpj += str(digito)

        return True if cnpj == cnpjOriginal else False

    except:
        return False


def gerar_cnpj(mascara=True):
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}'

    digito = calcula_digito(inicio_cnpj, 5)
    inicio_cnpj += str(digito)

    digito = calcula_digito(inicio_cnpj, 6)
    inicio_cnpj += str(digito)

    if validar_cnpj(inicio_cnpj):
        return mascara_cnpj(inicio_cnpj) if mascara else inicio_cnpj
    else:
        return gerar_cnpj()


if __name__ == '__main__':
    cnpj = '59.804.695/0001-07'
    # print(mascara_cnpj(cnpj))

    # print(validar_cnpj(cnpj))

    print(gerar_cnpj())
