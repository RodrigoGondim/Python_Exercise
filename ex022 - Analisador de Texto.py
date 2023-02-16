'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

# Input do nome
your_name = str(input('Digite seu nome completo: ')).strip()

# O nome com todas as letras maiúsculas e minúsculas.
your_name_lower = your_name.lower()
your_name_upper = your_name.upper()
print(f'Seu nome em minúsculas fica: {your_name_lower}')
print(f'Seu nome em maiúsculas fica: {your_name_upper}')

# Quantas letras sem os espaços.
your_name_count = len(your_name) - your_name.count(' ')
print(f'Seu nome tem {your_name_count} letras.')

# Quantas letras tem o primeiro nome.
your_name_split = your_name.split()
print(f'Seu primeiro nome é {your_name_split[0]} e tem {len(your_name_split[0])} letras')




