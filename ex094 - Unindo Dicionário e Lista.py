"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

population = list()
people = dict()
sum_age = average_age = 0

while True:
    people.clear()
    people['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        people['Sexo'] = str(input('Sexo[M/F/O]: ')).upper()[0]
        if people['Sexo'] in 'MFO':
            break
        print('Erro! Digite M/F/O')
    people['Idade'] = int(input('Idade: '))
    sum_age += people['Idade']
    population.append(people.copy())
    while True:
        option = str(input('Continuar[S/N]: ')).upper()[0]
        if option in 'SN':
            break
        print('Erro! Digite S/N')
    if option == 'N':
        break
print('=-' * 30)

# Letra A
print(f'Ao todo temos {len(population)} pessoas cadastradas.')

# Letra B
average_age = sum_age / len(population)
print(f'A média das idades é de {average_age:5.2f} anos ')

# Letra C
print('As mulheres cadastradas foram: ',end='')
for c in population:
    if c['Sexo'] in 'F':
        print(f'{c["Nome"]}', end=' ')

# Letra D
print(f'\nA lista de pessoas acima da média: ')
for c in population:
    if c['Idade'] >= average_age:
        print('   ')
        for k, v in c.items():
            print(f'{k}: {v} ')
        print()
