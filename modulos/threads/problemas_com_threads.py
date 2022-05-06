from threading import Thread
from time import sleep
from threading import Lock


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, qtd):
        self.lock.acquire()

        if self.estoque < qtd:
            print('Não temos ingressos')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= qtd
        print(f'Você comprou {qtd} ingresso(s). Ainda temos {self.estoque} disponiveís')

        self.lock.release()


if __name__ == '__main__':
    ing = Ingressos(10)
    # ing.comprar(1)
    # ing.comprar(1)
    # ing.comprar(1)
    # ing.comprar(1)
    # ing.comprar(1)

    threads = []
    for i in range(1, 20):
        t = Thread(target=ing.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:

        for t in threads:
            if not t.is_alive():
                executando = False
                break

    if not executando:
        print(ing.estoque)
