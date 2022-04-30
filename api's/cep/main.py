from cep import *
from enum import Enum, auto


while True:
    endereco = Cep.gerar_endereco()
    # print(endereco)
    c1 = Cep(endereco['cep'], ApiCep.VIA_CEP)
    print('\t',c1.buscar_cep())
    print('\n')
