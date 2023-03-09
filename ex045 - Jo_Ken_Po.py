'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

# Importações
from random import randint
from random import choice
from time import sleep

# Jogadas do user/pc
itens = ('Pedra', 'Papel', 'Tesoura')
round_pc = randint(0, 2)
round_user = int(input('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] Tesoura
Qual a sua jogada: '''))
print('=' * 25)

# Momento de espera do jogo - sleep
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('=' * 25)

# Print das jogadas
print(f'Computador jogou {itens[round_pc]}.')
print(f'Você jogou {itens[round_user]}.')
print('=' * 25)

# Menssagem de vitória / derrota
win_user = ['Você Ganhou!!!', 'Boa Jogada', 'VENCEDOR!']
lose_user = ['Você PERDEU!', 'Boa sorte na proxima', 'Você precisa treinar mais!']
draw = ['EMPATE!', 'Briga de titãs!', 'Duelo justo!']
win_user = choice(win_user)
lose_user = choice(lose_user)
draw = choice(draw)

# Condicionais
if round_pc == 0: # Pc jogou Pedra
    if round_user == 0:
        print(draw)
    elif round_user == 1:
        print(win_user)
    elif round_user == 2:
        print(lose_user)
    else:
        print('Jogada Inválida')
elif round_pc == 1: # Pc jogou Papel
    if round_user == 0:
        print(lose_user)
    elif round_user == 1:
        print(draw)
    elif round_user == 2:
        print(win_user)
    else:
        print('Jogada Inválida')
else:# Pc jogou Tesoura
    if round_user == 0:
        print(win_user)
    elif round_user == 1:
        print(lose_user)
    elif round_user == 2:
        print(draw)
    else:
        print('Jogada Inválida')