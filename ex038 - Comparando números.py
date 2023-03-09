'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

# 2 input de valor inteiro
fist_number = int(input('Digite um valor: '))
second_number = int(input('Digite um valor: '))

# Comparativos
if fist_number > second_number:
    print(f'{fist_number} é maior número')
elif second_number > fist_number:
    print(f'{second_number} é o maior número')
else:
    print('Os dois valores são IGUAIS')
