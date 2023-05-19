"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

# Criando uma matriz 3x3 + váriaveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_odd = bigger = sum_column = 0

# Lendo valores da matriz
for line in range(0, 3):
    for collumn in range(0, 3):
        matriz[line][collumn] = int(input(f'Digite um valor para [{line}, {collumn}]: '))

# Imprimindo a matriz na tela com formatação correta
for line in range(0, 3):
    for collumn in range(0, 3):
        print(f'[{matriz[line][collumn]:^5}]', end='')
        if matriz [line][collumn] % 2 == 0:
            sum_odd += matriz[line][collumn]
    print()
print('-=' * 30)

# Letra A
print(f'A soma dos números pares é: {sum_odd}')

# Letra B
for line in range(0, 3):
    sum_column += matriz[line][2]
print(f'A soma dos valores da 3° coluna é: {sum_column}')

# Letra C
for collumn in range(0, 3):
    if collumn == 0:
        bigger = matriz[1][collumn]
    elif matriz[1][collumn] > bigger:
        bigger = matriz[1][collumn]
print(f'O maior valor da segunda linha é:  {bigger}')
