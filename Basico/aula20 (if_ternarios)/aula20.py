logged = True

msg = 'Usuario Logado' if logged else 'Usuario não logado'

print(msg)


idade = input('Digite a sua idade: ')

if not  idade.isnumeric():
    print('Digite apenas números')
else:
    msg = 'Pode acessar' if int(idade)>=18 else 'Não pode acessar'
    print(msg)


string = 'dia'

msg = 'Está claro' if string == 'dia' else 'Está escuro'
print(msg)
