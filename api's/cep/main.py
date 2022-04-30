from cep import Cep


endereco = Cep.gerar_endereco()
print(endereco)
c1 = Cep(endereco['cep'])
print(c1.buscar_cep())
