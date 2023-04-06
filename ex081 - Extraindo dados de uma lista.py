"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

# Criação da lista
number_list = []
option = ''

while True:
    number_list.append(int(input('Digite um valor: ')))
    option = str(input('Continuar? [S/N] ')).strip().upper()
    if option in 'Nn':
        break
print(f'Sua lista: {number_list}')

# Letra A - len()
print(f'Ela tem {len(number_list)} Elementos.')

# Letra B - .sort(reverse=True)
print(f'A ordem reversa da lista é: {number_list.sort(reverse=True)}')

# Letra C - 'in'
if 5 in number_list:
    print('O valor 5 está na lista')
else:
    print('O valor 5 NÃO está na lista')
