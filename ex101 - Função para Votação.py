"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
 nas eleições."""


def voto(year):
    from datetime import date
    year_today = date.today().year
    age = year_today - year
    if age < 16:
        return f'Com {age} anos , NÃO pode votar'
    elif 16 <= age < 18 or age > 65:
        return f'Com {age} anos, o voto é OPCIONAL'
    else:
        return f'Com {age} anos, o voto é OBRIGATÓRIO'


born_year = int(input('Em que ano você nasceu: '))
print(voto(born_year))
