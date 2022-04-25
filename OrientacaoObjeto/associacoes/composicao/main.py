from cliente import Cliente

cliente = Cliente('julio', 'A')
cliente.inserir_endereco('13570-98', 'A21')
cliente.inserir_endereco('11570-08', 'Sala 2')
cliente.listar_enderecos()
del cliente

print('\n###################################################\n')

cliente2 = Cliente('maria', 'f')
cliente2.inserir_endereco('1458956', '85')
cliente2.inserir_endereco('1458965', '52')
cliente2.listar_enderecos()
del cliente2

