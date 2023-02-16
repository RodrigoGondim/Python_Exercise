'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

# Input do nome completo
your_name = str(input('Digite o seu nome completo: ')).strip()

# Mostrando o primeiro nome
print(f'Seu primeiro nome é: {your_name.split()[0].capitalize()}')

# Monstrando o último nome
print(f'Seu último nome é: {your_name.split()[-1].capitalize()}')

