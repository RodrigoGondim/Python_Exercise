"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

list_int_number = []

for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0 or x > list_int_number[len(list_int_number) - 1]:  # Adiciona se for o 1° Valor ou se for o último valor
        list_int_number.append(x)
    else:
        count = 0
        while count < len(list_int_number):
            if x <= list_int_number[count]:
                list_int_number.insert(count, x)
                break
            count += 1

print(f'Os valores digitados em ordem foram: {list_int_number}')
