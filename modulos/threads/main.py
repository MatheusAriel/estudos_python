from threading import Thread
from time import sleep


class MinhaThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MinhaThread('Thread 1', 3)
t1.start()

t2 = MinhaThread('Thread 2', 4)
t2.start()

t3 = MinhaThread('Thread 3', 1)
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
