'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
any_float_number = float(input('Escolha um número para ver a sua parte inteira: '))
print(f'O número que você escolheu foi {any_float_number} e sua parte inteira é {any_float_number.__trunc__()}')

