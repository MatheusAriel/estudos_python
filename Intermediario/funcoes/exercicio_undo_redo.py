def inserir_tarefa(list_tarefas, copy_list_tarefa):
    tarefa_input = input('Escreva a Tarefa nova: ')
    list_tarefas.append(tarefa_input)
    copy_list_tarefa.append(tarefa_input)


def listar_tarefas(list_tarefas):
    if len(list_tarefas) > 0:
        print('\nSua Lista de tarefas é: ')
        for i, tarefa in enumerate(list_tarefas, 1):
            print(f'\t{i} - {tarefa}')
    else:
        print('Sua lista está vazia')


def undo(list_tarefas):
    if len(list_tarefas) > 0:
        list_tarefas.pop()
        print('Desfeito com sucesso')
    else:
        print('Sua lista está vazia')


def refazer(list_tarefas, list_copy_tarefas):
    if len(list_copy_tarefas) > 0:
        if len(list_copy_tarefas) > len(list_tarefas):
            list_tarefas.append(list_copy_tarefas[-1])
            print('Refeito com sucesso')
        else:
            print('Lista já esta refeita por completa')
    else:
        print('Sua lista está vazia')


if __name__ == '__main__':
    list_tarefas = []
    copy_list_tarefas = []

    while True:
        print('1 - Inserir Tarefas\n2 - Listar tarefas\n3 - Desfazer\n4 - Refazer')
        op = input('\nDigite sua opção: ')

        if op == '1':
            inserir_tarefa(list_tarefas, copy_list_tarefas)

        elif op == '2':
            listar_tarefas(list_tarefas)

        elif op == '3':
            undo(list_tarefas)

        elif op == '4':
            refazer(list_tarefas, copy_list_tarefas)

        else:
            print('Opção inválida')

        print('\n###################\n')
        continue
