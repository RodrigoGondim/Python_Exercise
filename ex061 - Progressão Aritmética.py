"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while."""

# Inputs + Contadores
print('Gerador de PA')
print('*=' * 15)
first_term = int(input('Primeiro termo: '))
between_term = int(input('Razão: '))
termo = first_term
count = 1

# Repetição while
while count <= 10:
    print(f'{termo}', end=' ')
    termo += between_term
    count += 1
