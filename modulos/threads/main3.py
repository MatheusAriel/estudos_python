from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Thread 1', 5))
t1.start()



while t1.is_alive():
    print('Esperando a thread')
    sleep(2)

print('Thread acabou',end='\n********************************************\n\n')


t2 = Thread(target=vai_demorar, args=('Thread 2', 5))
t2.start()
t2.join()
print('Thread acabou')
