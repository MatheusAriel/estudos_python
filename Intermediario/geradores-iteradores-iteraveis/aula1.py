import sys
import time

string = 'Matheus'
print(hasattr(string, '__iter__'))
print()

l1 = list(range(10))
print(hasattr(l1, '__iter__'))  # mostra se eh iteravel ou n:  hasattr(l1, '__iter__')
print(hasattr(l1, '__next__'))  # mostra se eh interador ou n:  hasattr(l1, '__next__')

print()
iterador = iter(l1)
print(hasattr(iterador, '__next__'))
print(iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))

print()
l2 = list(range(1000))
print(f'A lista l1 esta consumindo {sys.getsizeof(l1)} bytes')
print(f'A lista l2 esta consumindo {sys.getsizeof(l2)} bytes')

print()


def gera(len=100):
    array = []
    for v in range(len):
        array.append(v)
        time.sleep(0.1)
    return array


"""
v = gera()
for i in v:
    print(i)
"""


def gerador(len=100):
    for v in range(len):
        yield v
        time.sleep(0.1)


v2 = gerador(5)
print(hasattr(v2, '__next__'))
print(hasattr(v2, '__iter__'))
print(next(v2))
print(next(v2))

print()
for i in v2:
    print(i)

print()


def gerador2():
    string = 'M'
    yield string
    string = 'a'
    yield string
    string = 't'
    yield string


g = gerador2()
print(next(g))
print(next(g))

print()
lista1 = [x for x in range(10)]
print(sys.getsizeof(lista1), type(lista1))

lista2 = (x for x in lista1)
print(sys.getsizeof(lista2), type(lista2))
print()
for v in lista2:
    print(v)
