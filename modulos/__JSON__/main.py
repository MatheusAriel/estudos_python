"""
https://docs.python.org/3/library/json.html


JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python   TO      JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON    TO  	Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""
from dados import *
import json

list = [1, 2, 3, 4, 5, 6, 7, 8]

#passar de PYTHON para JSON
json_list = json.dumps(list)
print(json_list, type(json_list))

print()

json_dict = json.dumps(clientes_dicionario, indent=4)
print(json_dict, type(json_dict))


print('\n\n')
#passar de JSON para PYTHON
dados_dict = json.loads(clientes_json)
print(dados_dict, type(dados_dict))
for k, v in dados_dict.items():
    print(k)
    print(v)


