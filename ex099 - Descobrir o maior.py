"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
 inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

# Função tratando os valores sem uso de Tupla()
def bigger(* num):
    size = len(num)
    bigger_num = count = 0

    print('Analisando os valores...')
    sleep(1)
    print(f'Foram informados {size} números.')
    print(f'Sua listagem: ', end=' ')
    for value in num:
        print(f'{value}', end=' ')
        if count == 0:
            bigger_num = value
        else:
            if value > bigger_num:
                bigger_num = value
        count += 1
    print()
    print(f'O maior valor é: {bigger_num} ')

    print('-' * 30)
    print()
    sleep(2)


# Programa Principal
bigger(2, 5, 5, 6, 9)
bigger(5, 8)
bigger(1, 2, 3)
bigger(5, 4, 7, 3, 4, 2)
bigger()
