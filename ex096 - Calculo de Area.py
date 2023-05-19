"""Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno."""


def area(height, length):
    area = height * length
    print(f'A área de um terreno de {height} X {length} é de {area:.2f}m²')


print('Controle de Terreno')
heigth = float(input('Altura (m): '))
length = float(input('Comprimento (m): '))
area(heigth, length)


