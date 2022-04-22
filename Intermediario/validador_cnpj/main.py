import cnpj

print(cnpj.gerar_cnpj())

while True:
    cnpj_input = input('Digite seu CNPJ: ')
    if cnpj.validar_cnpj(cnpj_input):
        print(f'O CNPJ: {cnpj_input} é VÁLIDO')
    else:
        print(f'O CNPJ: {cnpj_input} é INVÁLIDO')


