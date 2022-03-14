x = 0

while x <= 10:
    if (x == 0):
        x = x + 1
        continue
    print(x, '\n')
    x += 1

x = acumulador = 1

while x <= 10:
    if (x == 6):
        break
    print(x, acumulador)
    acumulador = acumulador + x
    x += 1
else:
    print('Final do while - só chega aqui quando der false no while')

nova_frase = ''
frase = 'O rato roeu a roupa do rei de Roma'
y = 0

while y < len(frase):
    print(frase[y])
    if frase[y] != ' ':
        nova_frase += frase[y]
    y += 1

print('\n', nova_frase)
