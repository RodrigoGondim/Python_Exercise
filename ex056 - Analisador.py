"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

# Variaveis e contadores
avarage_age = sum_age = 0
oldman_name = oldman_age = 0
yong_lady_count = 0

# Laço for
for c in range(1, 5):
    print(f'Analisando a {c}° Pessoa')
    name = str(input('Nome: ')).strip().capitalize()
    age = int(input('Idade: '))
    genre = str(input('Sexo M/F: ')).strip()
    sum_age += age
    if c == 1 and genre in 'Mn':
        oldman_name = name
        oldman_age = age
    if genre in 'Mm' and age > oldman_age:
        oldman_age = age
        oldman_name = name
    if genre in 'Ff' and age < 20:
        yong_lady_count += 1

avarage_age = sum_age / 4

# Print das informações solicitadas
print(f'A média de idade do grupo é de {avarage_age} anos.')
print(f'O homem mais velho tem {oldman_age} anos e seu nome {oldman_name} ')
print(f'Ao todo são {yong_lady_count} mulheres com menos de 21 anos.')
