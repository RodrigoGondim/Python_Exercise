"""Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

# Contadores das Letras 'A', 'B' e 'C'
count_age = count_man = count_young_women = 0

# Repetiçção while para aceitar somente os inputs 'corretos'
while True:
    print('=' * 25)
    print('CADASTRO DE PESSOAS')
    age = int(input('Idade: '))
    if age > 18:
        count_age += 1
    genre = ' '
    while genre not in 'MF':
        genre = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if genre == 'M':
        count_man += 1
    if age < 20 and genre == 'F':
        count_young_women += 1
    option = ' '
    while option not in 'SN':
        option = str(input('Quer Continuar [S/N]? ')).strip().upper()[0]
    if option == 'N':
        break

# Verificação dos contadores
print(f'Foram cadatrados {count_age} pessoas maior de 18 anos.')
print(f'Foram cadastrados {count_man} Homens.')
print(f'Foram cadastradas {count_young_women} Mulheres com menos de 20 anos')
