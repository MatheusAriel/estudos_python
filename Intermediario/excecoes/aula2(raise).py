def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(f'Error: {error}\n\n')
        raise


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(f'Error out function: {error}\n\n')

print()


def divide(n1, n2):
    if (n2 == 0):
        # lançando uma exception
        raise ValueError("Segundo número não pode ser 0")
    return n1 / n2


try:
    print(divide(2, 0))
except ValueError as error:
    print(f'Erro: {error}\n\n')
