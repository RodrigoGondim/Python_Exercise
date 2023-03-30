"""Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre elas (desconsiderando o flag)."""

# Criação do contador e 'somador'
count_number = sum_number = 0

# While Verdadeiro com uso do BREAK na flag 999
while True:
    int_number = int(input('Digite um número (999 para parar): '))
    if int_number == 999:
        break
    count_number += 1
    sum_number += int_number

# Print do contador e do somador dos números
print(f'Você digitou {count_number} números e sua soma foi {sum_number}')
