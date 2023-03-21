"""Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag)."""

# Input + contadores
int_number = int(input('Digite um valor: '))
count_number = 0
sum_number = 0

# While com FLAG de 999 no input
while int_number != 999:
    sum_number += int_number  # Se por o sum_number abaixo do contador, vá dar errado pois ele somará a FLAG
    count_number += 1
    int_number = int(input('Digite um valor: [999 para parar] '))
print(f'A soma dos {count_number} digitados foi de {sum_number}')
