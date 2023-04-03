"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
 mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares"""

# Ler 4 números e adicionar na Tupla
tuple_int_number = (int(input('Digite o 1° número: ')), int(input('Digite o 2° número: ')),
                    int(input('Digite o 3° número: ')), int(input('Digite o 4° número: ')))

# Contador do número 9
print(f'O número 9 apareceu {tuple_int_number.count(9)} vezes.')

# Posição do 1° números 3
if 3 in tuple_int_number:
    print(f'O valor 3 apareceu no {tuple_int_number.index(3) + 1}° número')
else:
    print('O número 3 NÃO apareceu.')

# Quais foram Pares
print('Os valores PARES digitados foram: ')
for c in tuple_int_number:
    if c % 2 == 0:
        print(c, end=' ')
