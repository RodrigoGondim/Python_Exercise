'''Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

# input do ano + importação
from datetime import date
year = int(input('Digite o ano para saber se ele é BISSEXTO (0 para ano atual): '))

# Ano atual do PC
if year == 0:
    year = date.today().year

# Condicionais
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} é BISSEXTO.')
else:
    print(f'O ano de {year} não é bissexto.')
