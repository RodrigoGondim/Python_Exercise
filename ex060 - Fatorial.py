"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

# Input + Contadores
int_number = int(input('Digite um número para calcular seu Fatorial: '))
count = int_number
factorial = 1

# Repetição While
print(f'Calculando {int_number}! =  ', end='')
while count > 0:
    print(f'{count}', end=' ')
    if count > 1:
        print('x ', end='')
    else:
        print('=')
    factorial *= count
    count -= 1
print(f'{factorial}')

# Easy mode
"""from math import factorial

int_number = int(input('Digite um número para calcular seu Fatorial: '))
fatctorial = factorial(int_number)

print(f'O fatorial de {int_number} é {fatctorial}')"""
