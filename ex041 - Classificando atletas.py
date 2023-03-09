'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date

# Input Nascimento + Calculo de idade
year_of_birth = int(input('Ano do nascimento: '))
year_today = date.today().year
age = year_today - year_of_birth

# Classificação
print(f'O atleta tem {age} de idade.')
if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Clasificação: INFANTIL')
elif age <= 19:
    print('Classificação: JÚNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Clasificação: MASTER')