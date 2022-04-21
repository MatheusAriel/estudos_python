import json

with open('pessoas.json', 'r') as file:
    dict_json = file.read()
    dict_json = json.loads(dict_json)
    print(dict_json, '\n\n')

for k, v in dict_json.items():
    print(f'{k}:')
    for k2, v2 in v.items():
        print(f'\t{k2}: {v2}')
    print('*****')
