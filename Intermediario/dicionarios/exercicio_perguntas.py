"""
jogo de perguntas e respostas com cadastro de perguntas e respostas
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 7*8? ',
        'respostas': {
            'a': '87',
            'b': '46',
            'c': '56',
            'd': '66',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 200x85? ',
        'respostas': {
            'a': '17000',
            'b': '15600',
            'c': '85600',
            'd': '85599',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 4x8? ',
        'respostas': {
            'a': '48',
            'b': '59',
            'c': '32',
            'd': '31',
        },
        'resposta_certa': 'c',
    }
}


def imprime_perguntas():
    for pk, pv in perguntas.items():
        print(f'{pk}: ')
        print(f'\t{pv["pergunta"]}')
        for rk, rv in pv['respostas'].items():
            print(f'\t\t[{rk}] : {rv}')
        print('\n')


def jogo(qtd_perguntas):
    pontos = 0
    for pk, pv in perguntas.items():
        while True:
            respostaincorreta = False
            print(f"{pk}: {pv['pergunta']}")
            for rk, rv in pv['respostas'].items():
                print(f'\t[{rk}] : {rv}')
            resposta_usuario = input('Qual a resposta certa? ').lower()
            if resposta_usuario not in pv['respostas'].keys():
                print('Digite uma alternativa válida ')
            else:
                respostaincorreta = True
                resposta_certa = pv['resposta_certa']
                if resposta_usuario == resposta_certa:
                    pontos += 1
                    print('\tVocê acertou')
                else:
                    print('\tVocê errou')
            if respostaincorreta:
                break
        print('\n')

    print(f'\nVocê acertou {pontos} de {qtd_perguntas} perguntas')
    print(f'Sua porcentagem de acerto foi de {pontos / qtd_perguntas * 100:.2f}%')


imprime_perguntas()
qtd_perguntas = len(perguntas)
alternativas = [chr(n).lower() for n in range(ord('a'), ord('d') + 1)]
if input('Deseja cadastrar mais perguntas? ').upper() == 'SIM':
    qtd_perguntas += 1
    while True:
        pergunta = input('Digite a pergunta: ')
        respostas = {}
        for a in alternativas:
            respostas[a] = input(f'Informe a alternativa {a}: ')

        while True:
            resposta_certa = input(f'Qual a alternativa correta {" | ".join(alternativas)} ?: ').lower()
            if resposta_certa in alternativas:
                break

        perguntas[f'Pergunta {qtd_perguntas}'] = {
            'pergunta': pergunta,
            'respostas': respostas,
            'resposta_certa': resposta_certa
        }

        if input('Deseja cadastrar outra pergunta? ').upper() == 'NAO':
            imprime_perguntas()
            qtd_perguntas = len(perguntas)
            break

if input('Deseja começar o jogo ?').upper() == 'SIM':
    print('\n\n\n\ \t**********************\tBOA SORTE\t*******************************\t')
    jogo(qtd_perguntas)
