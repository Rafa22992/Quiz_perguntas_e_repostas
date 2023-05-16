# Aula 124 ex com dicionario
from os import system

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': 'C',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': 'A',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': 'B',
    },
]
def question_system(chave):
    ch_dict_1 = ''
    ch_dict_2 = ''
    ch_dict_3 = ''

    for p in perguntas:
        chaves_dict = p[chave]
        
        if ch_dict_1 == '':
            ch_dict_1 = chaves_dict
            continue

        if ch_dict_2 == '':
            ch_dict_2 = chaves_dict
            continue

        if ch_dict_3 == '':
            ch_dict_3 = chaves_dict
            break

    return ch_dict_1,ch_dict_2,ch_dict_3

def limpa_tela():
    return system('cls')

questionario = question_system('Pergunta')
opcoes = question_system('Opções')
resposta_certa = question_system('Resposta')

print('=' * 35)
print(f'{"QUIZ":-^35}')
print('=' * 35)

certas = 0
erradas = 0

n_pergunta = 1
indice = 0
while indice < 3:
    mostra_questoes = questionario[indice]
    print(f'Pergunta: {n_pergunta} {mostra_questoes}')
    n_pergunta += 1

    alternativas = opcoes[indice]

    for alternativa_letra,opcoes_questoes in enumerate(alternativas):

        if int(alternativa_letra) == 0:
            alternativa_letra = 'A'
            print(f'{alternativa_letra}- {opcoes_questoes}')

        if alternativa_letra == 1:
            alternativa_letra = 'B'
            print(f'{alternativa_letra}- {opcoes_questoes}')

        if alternativa_letra == 2:
            alternativa_letra = 'C'
            print(f'{alternativa_letra}- {opcoes_questoes}')

        if alternativa_letra == 3:
            alternativa_letra = 'D'
            print(f'{alternativa_letra}- {opcoes_questoes}')

    print('-' * 35)
    resposta_usuario = input('Resposta: ').upper()
    print('-' * 35)
    new_screen = limpa_tela()

    corretas = resposta_certa[indice]

    if resposta_usuario == corretas:
        print('Acertou')
        certas += 1
    
    else:
        print('Errou')
        erradas += 1

    indice += 1

print(f'Você acertou {certas} perguntas e errou {erradas}')
print(f'Em um total de {indice} perguntas!!!')
print('-' * 35)