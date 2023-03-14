"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
 ainda não atingiram a maioridade e quantas já são maiores."""

# Importação + criação de contadores
from datetime import date
year_today = date.today().year
yong_people = old_people = 0

# Repetição 'for' input + contadores
for c in range(1, 8):
    born_year = int(input(f'Em que ano nasceu a {c}° Pessoa: '))
    if year_today - born_year < 21:
        yong_people += 1
    else:
        old_people += 1
print(f'Ao todo tivemos {yong_people} mais novas e {old_people} mais velhas.')
