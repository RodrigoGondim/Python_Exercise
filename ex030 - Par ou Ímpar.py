'''Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

# input de um número int
any_number_int = int(input('Digite qualquer número inteiro: '))

# Condicionais
if any_number_int % 2 == 0: # OU any_number_int % 2 == 1 ;para ser ímpar
    print(f'O número {any_number_int} é PAR')
else :
    print(f'O número {any_number_int} é ÍMPAR')
