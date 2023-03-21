"""Exercício Python 059: Crie um programa que leia dois valores inteiros e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

# Importação para 'firula'
from time import sleep

# Criação das variáveis
number_1 = int(input('Primeiro valor : '))
number_2 = int(input('Segundo valor: '))
option = 0

# Repetição do menu em condicionais
while option != 5:
    sleep(0.5)
    print('''Operaçãoes: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    option = int(input('Qual a sua opção : '))

    if option == 1:  # SOMA
        print(f'A soma de {number_1} + {number_2} = {number_1 + number_2}')
    elif option == 2:  # MULTIPLICAÇÃO
        print(f'A multiplicação de {number_1} X {number_2} = {number_1 * number_2}')
    elif option == 3:  # MAIOR VALOR
        if number_1 > number_2:
            print(f'O primeiro valor({number_1}) é maior que o segundo valor ({number_2})')
        elif number_1 < number_2:
            print(f'O segundo valor ({number_2}) é maior que o primeiro valor ({number_1})')
        else:
            print('Ambos tem o mesmo valor.')
    elif option == 4:  # NOVAS ENTRADAS
        print('Você quer novos valores.')
        number_1 = float(input('Primeiro valor : '))
        number_2 = float(input('Segundo valor: '))
    elif option == 5:  # ENCERRAMENTO DO WHILE ainda sem o uso do BREAK
        print('Encerrando o programa!')
        sleep(1)
    else:  # Opção inválida
        print('Opção inválida. Tente outra')

print('FIM')
