from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from banco import Banco

try:
    cliente1 = Cliente('matheus souza', 28, '918.830.920-78')
    # cliente1.exibir_dados_clientes()

    cliente2 = Cliente('Camila Maria', 33, '159.174.610-82')
    # cliente2.exibir_dados_clientes()

    cliente3 = Cliente('Gilberto Ronsenberg', 19, '039.782.270-70')
    # cliente3.exibir_dados_clientes()

    conta_corrente1 = ContaCorrente('AG0001', 'CC878', 0)

    print('\n\n\n**************************************************************************\n\n\n')

    conta_poupanca = ContaPoupanca('AG0001', 'CC5230-0', 1000)
    conta_poupanca2 = ContaPoupanca('AG0004', 'CC5230-1', 1000)

    print('\n\n\n**************************************************************************\n\n\n')
    banco1 = Banco('Santander', ['AG0001', 'AG0002', 'AG0004'])

    banco1.inserir_cliente(cliente1)
    # banco1.inserir_cliente(cliente1)
    banco1.inseir_conta(conta_poupanca)
    banco1.inseir_conta(conta_poupanca2)
    banco1.autenticar(cliente3)

    conta_corrente1.depositar(1200)
    conta_corrente1.depositar(200)
    conta_corrente1.sacar(10)

    conta_poupanca.depositar(200)
    conta_poupanca.depositar(200)

    conta_poupanca2.depositar(200)
    conta_poupanca2.depositar(200)
except Exception as error:
    print(f'Erro - {error}')
