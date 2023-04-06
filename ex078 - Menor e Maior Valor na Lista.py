"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista. """


list_int_number = []
smaller_number = bigger_number = 0

for c in range(0, 5):
    list_int_number.append(int(input(f'Digite um número na posição {c}°: ')))
    if c == 0:
        smaller_number = bigger_number = list_int_number[0]
    else:
        if list_int_number[c] < smaller_number:
            smaller_number = list_int_number[c]
        elif list_int_number[c] > bigger_number:
            bigger_number = list_int_number[c]

print(f'Você digitou os valores: {list_int_number}')
print(f'O menor valor digitado foi: {smaller_number} nas posições', end=' ')
print(f'O maior valor digitado foi: {bigger_number}')
