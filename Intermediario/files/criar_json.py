import json

dict = {
    'Pessoa1': {
        'idade': 28,
        'nome': 'Matheus',
        'profissao': 'Dev'
    },
    'Pessoa2': {
        'idade': 29,
        'nome': 'Gilberto',
        'profissao': 'Advogado'
    },
    'Pessoa3': {
        'idade': 70,
        'nome': 'Antônio',
        'profissao': 'Aposentado'
    }
}

pessoas_json = json.dumps(dict, indent=True)

with open('pessoas.json', 'w+') as file:
    file.write(pessoas_json)
