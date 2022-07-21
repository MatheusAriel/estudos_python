import json
import urllib
import requests

# url = 'https://parseapi.back4app.com/classes/CEP?order=CEP,estado,cidade,bairro,logradouro,info,numero'
url = 'https://parseapi.back4app.com/graphql'

headers = {
    'X-Parse-Application-Id': 'QqDpRY6ILPi2ze5mPrSfLgoN3HuYLfJytg30AtBq',  # This is the fake app's application id
    'X-Parse-Master-Key': 'YqmyWSSMx8F17rGuWFJYYQ0SH734Im8KGCzn4FY5'  # This is the fake app's readonly master key
}

payload = {
    "operationName": "allCEPS",
    "variables":None,
    "query": "query allCEPS {\n      cEPS (skip: 0, limit: 3) {\n        results {\n          ACL\n          CEP\n          bairro\n          cidade\n          estado\n          info\n          logradouro\n          numero\n        }\n      }\n    } "
}

response = requests.post(url, json=payload, headers=headers)
print(response, response.json())

# data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
# print(json.dumps(data, indent=2))
