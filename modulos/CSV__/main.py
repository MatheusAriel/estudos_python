"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as file:
    # dados_csv = csv.reader(file)#assim retorna em lista

    #dados_csv = csv.DictReader(file, delimiter=';')
    dados_csv = csv.DictReader(file)

    # next(dados_csv)  # faz com q ignore a primeira linha em lista

    for dado in dados_csv:
        #print(dado)
        print(f'Nome: {dado["Nome"]}', sep=' | ')
        print(f'Sobrenome: {dado["Sobrenome"]}', sep=' | ')
        print(f'E-mail: {dado["E-mail"]}', sep=' | ')
        print(f'Telefone: {dado["Telefone"]}', end='\n\n' + '*' * 100 + '\n')

print('\n' + '#' * 100)

with open('clientes.csv', 'r') as file:
    dados2 = [x for x in csv.DictReader(file)]

for dados in dados2:
    print(dado)

print()

with open('clientes2.csv', 'w+') as file:
    escreve = csv.writer(
        file,
        delimiter=';',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    cabecalho = dados2[0].keys()
    cabecalho = list(cabecalho)

    escreve.writerow([
        cabecalho[0],
        cabecalho[1],
        cabecalho[2],
        cabecalho[-1]
    ])

    for dado in dados2:
        # print(dado['Nome'])
        escreve.writerow([
            dado['Nome'],
            dado['Sobrenome'],
            dado['E-mail'],
            dado['Telefone']
        ])
