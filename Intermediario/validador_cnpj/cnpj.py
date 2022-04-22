import re


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
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        raise 'CNPJ Sequencial'
    return True


def validador_cnpj(cnpj):
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


if __name__ == '__main__':
    cnpj = '59.804.695/0001-07'
    print(mascara_cnpj(cnpj))

    print(validador_cnpj(cnpj))
