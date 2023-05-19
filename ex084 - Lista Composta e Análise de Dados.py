"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas[100+Kg].
C) Uma listagem com as pessoas mais leves[-100kg]."""

main_list = []
temp_list = list()
smaller = bigger = 0

while True:
    temp_list.append(str(input('Nome: ')).strip().capitalize())
    temp_list.append(float(input('Peso: ')))
    if len(main_list) == 0:
        smaller = temp_list[1]
        bigger = temp_list[1]
    else:
        if temp_list[1] < smaller:
            smaller = temp_list[1]
        elif temp_list[1] > bigger:
            bigger = temp_list[1]
    main_list.append(temp_list[:])
    temp_list.clear()
    option = str(input('Continuar: [S/N] '))
    while option not in 'SsNn':
        option = str(input('Continuar: [S/N] ')).strip()[0]
    print('-' * 30)
    if option in 'Nn':
        break

print(f'Foram cadastradas {len(main_list)} pessoas.')
print(f'O menor peso foi de: {smaller}Kg.', end='')
for person in main_list:
    if person[1] == smaller:
        print(f'[{person[0]}]', end=' ')

print()

print(f'O maior peso foi de: {bigger}Kg.', end='')
for person in main_list:
    if person[1] == bigger:
        print(f'[{person[0]}]', end=' ')
