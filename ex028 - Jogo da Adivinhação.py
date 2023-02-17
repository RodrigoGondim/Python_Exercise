'''Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
 o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
 venceu ou perdeu.'''

# Número "escolhido" pelo PC + importações
from random import choice
from time import sleep
chosen_pc_number = [0, 1, 2, 3, 4, 5]
chosen_pc_number = choice(chosen_pc_number)

# Input do usuario para adivinhar o número que o PC escolheu
print('=*=' * 20)
print('Vou pensar em um número entra 0 e 5. Tente adivinhar...')
print('=*=' * 20)
chosen_user_number = int(input('Em que número eu pensei? '))

# Comparação do número com o input
print('Processando...')
sleep(1.5)
if chosen_pc_number == chosen_user_number:
    print('Parabéns, você ACERTOU!!!')
else:
    print(f'Você ERROU. Eu pensei no número {chosen_pc_number} e não no {chosen_user_number}')
