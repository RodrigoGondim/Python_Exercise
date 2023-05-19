"""Exercício Python 106: Faça um mini-sistema que utilize a ajuda interativa do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' ('END'), o programa será fechado. Importante: Use
cores."""

c = ('\033[m',  # 0 - sem cor
     '\033[0;30;41m',  # 1 - VERMELHO
     '\033[0;30;42m',  # 2 - VERDE
     '\033[0;30;43m',  # 3 - AMARELO
     '\033[0;30;44m',  # 4 - AZUL
     '\033[0;30;45m',  # 5 - ROXO
     '\033[7;30m'     # 6 - BRANCO
     )


def ajuda(com):
    titulo(f' Acessando o manual do comando\'{com}\'')
    print(c[4], end='')
    help(com)
    print(c[4], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[1], end='')


# Programa Principal
comando = ''
while True:
    titulo('Sistema de Ajuda PyDoc', 3)
    comando = str(input('Função ou lib: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo :)')
