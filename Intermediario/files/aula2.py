try:
    file = open('teste2.txt', 'w+')

    for i in range(10):
        file.write(f"Linha: {i + 1}\n")

    file.seek(0)
    print(file.readlines())

except Exception as error:
    print(f'Erro {error}')
finally:
    file.close()

# MELHOR JEITO
print('\n\n######### MELHOR MODO DE TRABALHAR COM ARQUIVOS EM PYTHON ##############\n\n')
with open('teste2.txt', 'a+') as file:
    file.write('ola')
    file.seek(0)
    print(file.readlines())
