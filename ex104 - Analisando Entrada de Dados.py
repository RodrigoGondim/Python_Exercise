"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""


def leiaint(num):
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            return num
            break
        else:
            print('ERRO! Digite um número inteiro válido')
            print('-' * 50)
            print()


# Programa principal
x = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {x}')
