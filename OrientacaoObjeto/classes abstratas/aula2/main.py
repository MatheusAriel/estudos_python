from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

try:
    print('Conta Poupança')
    cp = ContaPoupanca('ASX', 'SZ25', 100)
    cp.depositar(10)
    cp.sacar(99)
    cp.sacar(10)
    # cp.sacar(10)
    print('\n\n\t#################################################################\n\n')

    print('Conta Corrente')
    cc = ContaCorrente(agencia='1223A', conta='1022', saldo=0, limite=500)
    cc.depositar(100)
    cc.sacar(250)
    cc.depositar(600)
except ValueError as er:
    print(f'Erro - {er}')
except Exception as er:
    print(f'Erro - {er}')
