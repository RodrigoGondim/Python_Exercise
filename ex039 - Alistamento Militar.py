'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

# Input + importação
from datetime import date

year_of_birth = int(input('Ano do nascimento: '))
year_today = date.today().year
age = year_today - year_of_birth

# Print + Condicionais
print(f'Quem nasceu em {year_of_birth} tem {age} anos em {year_today}.')
if age < 18:
    print(f'Você ainda não precisa se alistar, seu alistamento será no ano de {year_of_birth + 18}')
elif age == 18:
    print('Este é o ano do seu Alistamento!')
else:
    print(f'Seu alistamento já passou e foi no ano de {year_of_birth + 18}.')







