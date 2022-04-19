"""
jogo de perguntas e respostas com cadastro de perguntas e respostas
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 7*8? ',
        'respostas': {
            'A': '87',
            'B': '46',
            'C': '56',
            'D': '66',
        },
        'resposta_certa': 'C',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 200x85? ',
        'respostas': {
            'A': '17000',
            'B': '15600',
            'C': '85600',
            'D': '85599',
        },
        'resposta_certa': 'A',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 4x8? ',
        'respostas': {
            'A': '48',
            'B': '59',
            'C': '32',
            'D': '31',
        },
        'resposta_certa': 'C',
    }
}


def imprime_perguntas():
    for pk, pv in perguntas.items():
        print(f'{pk}: ')
        print(f'\t{pv["pergunta"]}')
        for rk, rv in pv['respostas'].items():
            print(f'\t\t\t\t\t[{rk.upper()}] : {rv}')
        print('\n')


def jogo(qtd_perguntas):
    pontos = 0
    for pk, pv in perguntas.items():
        while True:
            resposta_incorreta = False
            print(f"{pk}: {pv['pergunta']}")
            for rk, rv in pv['respostas'].items():
                print(f'\t[{rk}] : {rv}')
            resposta_usuario = input('\tQual a resposta certa? ').upper()

            if resposta_usuario not in pv['respostas'].keys():
                print('Digite uma alternativa válida ')
            else:
                resposta_incorreta = True
                resposta_certa = pv['resposta_certa']
                if resposta_usuario == resposta_certa:
                    pontos += 1
                    print('\tVocê acertou')
                else:
                    print('\tVocê errou')
            if resposta_incorreta:
                break
        print('\n')

    print(f'\nVocê acertou {pontos} de {qtd_perguntas} perguntas')
    print(f'Sua porcentagem de acerto foi de {pontos / qtd_perguntas * 100:.2f}%')


imprime_perguntas()
qtd_perguntas = len(perguntas)
alternativas = [chr(n).upper() for n in range(ord('A'), ord('D') + 1)]
if input('Deseja cadastrar mais perguntas? [SIM - NAO]').upper() == 'SIM':
    qtd_perguntas += 1
    while True:
        pergunta = input('Digite a pergunta: ')
        respostas = {}
        for a in alternativas:
            respostas[a] = input(f'Informe a alternativa {a}: ')

        while True:
            resposta_certa = input(f'Qual a alternativa correta {" | ".join(alternativas)} ?: ').upper()
            if resposta_certa in alternativas:
                break

        perguntas[f'Pergunta {qtd_perguntas}'] = {
            'pergunta': pergunta,
            'respostas': respostas,
            'resposta_certa': resposta_certa
        }

        if input('Deseja cadastrar outra pergunta? [SIM - NAO]').upper() == 'NAO':
            imprime_perguntas()
            qtd_perguntas = len(perguntas)
            break

if input('Deseja começar o jogo? [SIM - NAO]').upper() == 'SIM':
    print('\n\n\n \t*****************************************\tBOA SORTE\t*****************************************\t')
    jogo(qtd_perguntas)
