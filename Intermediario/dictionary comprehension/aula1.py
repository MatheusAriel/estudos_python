l1 = [
    ('CHAVE1', 'valor1'),
    ('chave2', 'valor2')
]

d1 = {x.lower(): y.upper() + '_' for x, y in l1}
print(d1)

print()
d2 = {f'Chave: {x}': x * 10 for x in enumerate(range(10))}
print(d2, type(d2))
