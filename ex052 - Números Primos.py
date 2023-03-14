'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

# Input de um número inteiro + contador
int_number = int(input('Digite um número: '))
count = 0

# Repetição 'for'
for c in range(1, int_number + 1):
    if int_number % c == 0:
        print('\033[33m', end='') # Foi adicionar cor apenas para melhor visualização
        count += 1
    else:
        print('\033[31m', end='')# Foi adicionar cor apenas para melhor visualização
    print(c, end=' ')
print(f'\n\033[mO número {int_number} foi divisível {count} vezes.')
if count == 2:
    print(f'O número {int_number} é PRIMO.')
else:
    print(f'O número {int_number} NÃO é primo.')