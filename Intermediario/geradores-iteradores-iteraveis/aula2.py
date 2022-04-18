nome = "Matheus"
iterador = iter(nome)
gerador = (x for x in nome)


try:
    print(next(iterador))  # M
    print(next(iterador))  # A
    print(next(iterador))  # T
    print(next(iterador))  # H
    print(next(iterador))  # E
    print(next(iterador))  # U
    # print(next(iterador))#S

except:
    pass

print('Iterador Dentro do for')
for l in iterador:
    print(l)


print()
print(next(gerador))
print('Gerador Dentro do for')
for l in gerador:
    print(l)
