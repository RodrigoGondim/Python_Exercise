"""Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
 jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint  # Para a escolha do PC
from time import sleep  # Para Firula

# Apresentação do sistema + Contador de round
print('-' * 30)
print('Vamos Jogar PAR OU ÍMPAR')
print('-' * 30)
count = 0
even_or_odd = ' '

# While com Break somente quando se perde a partida
while True:
    pc_number = randint(0, 10)
    user_number = int(input('Digite um valor: '))
    while even_or_odd not in 'PpIi':
      even_or_odd = str(input('PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    total = pc_number + user_number
    sleep(1)
    if total % 2 == 0 and even_or_odd == 'P':
        print(f'Você jogou {user_number} e eu joguei {pc_number}. Total {total} é PAR')
        print('Você GANHOU')
        print('-' * 30)
        count += 1
    elif total % 2 == 1 and even_or_odd == 'I':
        print(f'Você jogou {user_number} e eu joguei {pc_number}. Total {total} é IMPAR')
        print('Voce GANHOU!')
        print('-' * 30)
        count += 1
    else:
        print(f'Você jogou {user_number} e eu joguei {pc_number}')
        print('Você PERDEU!')
        print('-' * 30)
        break
sleep(1)
print(f'GAME OVER! Você ganhou {count} vezes.')
