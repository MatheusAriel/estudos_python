file = open('teste.txt', 'w+')

for i in range(4):
    file.write(f"Linha {i + 1}\n")

print('Lendo op arquivo:\n')
file.seek(0, 0)
print(file.read())

file.seek(0, 0)
print('\n###########\n')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)
print('\n###########\n')
print(file.readlines())
for linha in file.readlines():
    print(linha, end='')


file.close()
