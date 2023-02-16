'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

# Lendo e tratando o input do nome
your_name = str(input('Digite o seu nome completo: ')).strip().upper()

# Verificando se tem 'SILVA' no nome
print('Seu nome tem SILVA?')
print('SILVA' in your_name)


