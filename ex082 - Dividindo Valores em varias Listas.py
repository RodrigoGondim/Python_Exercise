"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas."""

# Criação da lista + continue
list_number = []
list_number_odd = []
list_number_even = []

# Adicionando os valores para a 1° lista
while True:
    list_number.append(int(input('Digite um valor: ')))
    option = str(input('Continuar? [S/N]: ')).strip().upper()
    while option not in 'SsNn':
        option = str(input('Continuar? [S/N]: ')).strip().upper()
    if option in 'Nn':
        break

# Verificando Par/Ímpar e adicionando na suas listas
for i, v in enumerate(list_number):  # 'Para' Índice, 'Valores' enumerados da lista_number
    if v % 2 == 0:
        list_number_odd.append(v)
    elif v % 2 == 1:
        list_number_even.append(v)

# Prints das 3 listas solicitadas
print(f'Sua lista tem os valores: {list_number}')
print(f'Sua lista de Pares: {list_number_odd}')
print(f'Sua lista de Ímpares: {list_number_even}')
