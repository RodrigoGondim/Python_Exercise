"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
 mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

# Importação do random
from random import randint

# Randomizar 5 números inteiros e colocar em uma tupla
tuple_int_number = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))

print(f'Os números sorteados foram:', end=' ')
for c in tuple_int_number:  # Uso do 'for' apenas para ficar bonitinho no terminal
    print(f'{c}', end=' ')

# Maior e Menor Valor utilizando a função Max e min
print(f'\nO maior valor sorteado foi: {max(tuple_int_number)}')
print(f'O menor valor sorteado foi : {min(tuple_int_number)}')
