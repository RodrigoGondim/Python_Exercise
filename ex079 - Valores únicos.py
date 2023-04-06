"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. """

# Criação das Váriaveis
list_int_number = []
option = ' '

# Repetição while com o break em option
while True:
    x = int(input('Digite um valor: '))
    if x not in list_int_number:
        list_int_number.append(x)
    else:
        print('Valor já adicionado antes...')
    option = str(input('Continuar? [S/N] '))
    if option in 'Nn':
        break

# Ordenando em crescente a lista e printando
list_int_number.sort()
print(list_int_number)
