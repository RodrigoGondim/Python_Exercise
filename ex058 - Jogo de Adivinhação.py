"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

# Importações
from random import randint
from time import sleep

# 'Escolha' do pc + criação das variáveis
choice_pc_number = randint(0, 10)

print('''Olá, sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi ?''')

sleep(0.5)
count_try = 0
win = False

# Laço com condicional + contador de tentativas e variável de quebra
while not win:
    user_try = int(input('Qual é o seu palpite: '))
    if user_try == choice_pc_number:
        win = True
    else:
        if user_try < choice_pc_number:
            print('Maior...')
            count_try += 1
        elif user_try > choice_pc_number:
            print('Menor...')
            count_try += 1
print(f'Você acertou em {count_try + 1 } tentativas. Parabéns!')
