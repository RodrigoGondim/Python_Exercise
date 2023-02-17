'''Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

# 3 input de qualquer valor
fist_number = float(input('Digite um valor: '))
second_number = float(input('Digite um valor: '))
third_number = float(input('Digite um valor: '))

# Condicionais - Quem é o menor
smaller_number = fist_number
if second_number < fist_number and second_number < third_number:
    smaller_number = second_number
if third_number < fist_number and third_number < second_number:
    smaller_number = third_number

# Condicionais - Quem é o Maior
bigger_number = fist_number
if second_number > fist_number and second_number > third_number:
    bigger_number = second_number
if third_number > fist_number and third_number > second_number:
    bigger_number = third_number

# Print do menor e maior número
print(f'O menor número é {smaller_number}')
print(f'O maior número é {bigger_number}')

