"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formatação correta."""

# Criando uma matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Lendo valores da matriz
for line in range(0, 3):
    for collumn in range(0, 3):
        matriz[line][collumn] = int(input(f'Digite um valor para [{line}, {collumn}]: '))

# Imprimindo a matriz na tela com formatação correta
for line in range(0, 3):
    for collumn in range(0, 3):
        print(f'[{matriz[line][collumn]:^5}]', end='')
    print()
