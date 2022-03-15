texto = 'O rato roeu a roupa do rei de Roma'

for letra in texto:
    print(letra)

print()

for x, letra in enumerate(texto):
    print(x, letra)

print()

#range (start =0, stop, step=1)
for n in range(1, 100, 2):
    print(n)
