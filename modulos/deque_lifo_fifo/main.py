"""
PILHAS E FILAS

PILHA (STACK) - LIFO - Last IN, First Out
    exemplo: Pilha de livros que são adicionados um sobre o outro

FILA (QUEUE) - FIFO - First IN First Out
    exemplo: Uma fila de banco (ou qq outra fila do mundo real)

Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados
"""

from collections import deque
from time import sleep

fila = deque(maxlen=5)
print(fila, type(fila))

fila.append('João')
fila.append('Maria')
fila.append('Luiz')
fila.append('Marcos')
fila.append('José')


print(fila)

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

print('\n\n\n')

fila2 = deque(maxlen=10)
for i in range(1000):
    fila2.append(i)
    sleep(1)
    print(fila2)
