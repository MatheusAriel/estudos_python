import json
import urllib
import requests

headers = {
    'X-Parse-Application-Id': 'YEmr0qWmZ5OJPJOAecKyf1LDnPUXK9uqYhDKCHdm',
    'X-Parse-REST-API-Key': 'QQv4BXdgXtHEQpvIYuawq8HJjsGOXPxursTg1xsc'
}

skip = 1

while skip <= 10:
    url = f'https://parseapi.back4app.com/classes/Cepcorreios_CEP?skip={skip}&limit=10&order=estado,cidade'

    # data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))
    # print(json.dumps(data, indent=2))

    result = requests.get(url, headers=headers)
    print(result, result.json())
    skip += 1
