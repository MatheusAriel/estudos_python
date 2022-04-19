list_numeros = list(range(100))

pares = [n for n in list_numeros if n % 2 == 0]
impares = [n for n in list_numeros if n % 2 != 0]

print(f'Número pares: \n\t{pares}\n'
      f'Números ímpares: \n\t{impares}')
