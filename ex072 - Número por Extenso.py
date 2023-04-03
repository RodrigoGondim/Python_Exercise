"""Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    int_number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= int_number <= 20:  # Somente aceitar número entre 0 e 20
        break
    print('Tente novamente!')
    print('-' * 30)

print(f'Você digitou o número {extenso[int_number]}')
