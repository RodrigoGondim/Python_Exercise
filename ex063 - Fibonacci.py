"""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

# Input + Contador
int_number = int(input('Digite um número para saber sua sequencia de Fibonacci: '))
a = 0
b = 1
count = 3
print(f'{a} {b}', end=' ')

# A documentação ajudou MUITO na resolução
while count <= int_number:
    c = a + b
    print(f'{c}', end=' ')
    a = b
    b = c
    count += 1
print('FIM')
