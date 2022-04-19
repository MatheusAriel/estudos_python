def converte_numero(string):
    try:
        string = int(string)
        return string
    except ValueError:
        try:
            string = float(string)
            return string
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is not None:
        print(numero * 2)
    else:
        print('Digite um número valido\n')
