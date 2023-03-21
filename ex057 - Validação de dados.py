"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
esteja errado, peça a digitação novamente até ter um valor correto."""

genre = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

# While aceitando somente os valores permitidos
while genre not in 'MmFf':
    genre = str(input('Dados inválidos, informe seu sexo: M/F ')).strip().upper()[0]

print(f'Sexo {genre}. registrado!')
