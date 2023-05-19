"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
 início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

# Importação
from time import sleep


def count(start, end, steep):  # Função que trabalha como o Loop 'for'
    # Caso o steep seja 0 ou Negativo
    if start < 0:
        steep *= -1
    if steep == 0:
        steep = 1
    print(f'Contagem de {start} até {end} de {steep} em {steep}.')

    if start < end:
        cont = start
        while cont <= end:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += steep
        print('FIM')
    else:
        cont = start
        while cont >= end:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= steep
        print('FIM')


# Program Principal
count(1, 10, 1)  # Letra A
print()
count(10, 0, 2)  # Letra B
print()
print()
print('Agora é a sua vez de personalisar')
star_user = int(input('Inicio: '))
end_user = int(input('Fim: '))
steep_user = int(input('Passo: '))
count(star_user, end_user, steep_user)
