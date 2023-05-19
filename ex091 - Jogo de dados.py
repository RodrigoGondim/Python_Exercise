"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
 número no dado."""

# Importações
from random import randint
from time import sleep
from operator import itemgetter

# Criação do dicionário
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = []  # Poderia ser criado como um Dict mas o retorno seria em forma de List

# Print bonito na tela
for keys, values in jogo.items():
    print(f'{keys} tirou: {values}')
    sleep(0.5)

# Organizando o Dict/List do ranking
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=*' * 30)
print('  == RANKING DOS JOGADORES ==  ')

# Print bonito na tela utilizando manipulação de lista
for i, v in enumerate(ranking):
    print(f'{i + 1}° com {v[0]} com {v[1]}')
    sleep(1)

