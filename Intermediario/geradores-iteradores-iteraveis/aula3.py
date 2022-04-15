from types import GeneratorType

zip1 = zip('Alo', 'Alo')

print(isinstance(zip1, GeneratorType))

zip2 = ((x, y) for x, y in zip('Alo', 'Alo'))

print(isinstance(zip2, GeneratorType))

