'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a between_term de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

# Input da Prograssão
first_term = int(input('Primeiro termo: '))
between_term = int(input('Razão: '))
tenth_term = first_term + (10 - 1) * between_term

# Repetição 'for' usando os inputs necessários
for c in range(first_term, tenth_term + between_term, between_term):
    print(f'{c}', end=' ')
print('FIM!')
