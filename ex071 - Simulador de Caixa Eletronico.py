"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('=' * 30)
print('{:^30}'.format('BANK'))
print('=' * 30)
valor_saque = int(input('Digite o valor que deseja sacar: R$ '))

total = valor_saque
cedulas = 50
total_cedulas = 0

while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total == 0:
            break
