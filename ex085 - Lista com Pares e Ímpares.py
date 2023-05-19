"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os numa lista
 única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
."""

list_number = [[], []]
x = 0

for c in range(1, 8):
    x = int(input(f'Digite o {c}° valor: '))
    if x % 2 == 0:
        list_number[0].append(x)

    else:
        list_number[1].append(x)

list_number[0].sort()
list_number[1].sort()

print(f'A lista dos números pares foi: {list_number[0]}')
print(f'A lista dos números ímpares foi: {list_number[1]}')
