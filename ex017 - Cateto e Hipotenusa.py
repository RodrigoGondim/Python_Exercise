'''Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
triangle_side1 = float(input('Comprimento do cateto oposto: '))
triangle_side2 = float(input('Comprimento do cateto adjacente: '))
hypotenuse = hypot(triangle_side1, triangle_side2)
print(f'A Hipotenusa vai medir {hypotenuse:.2f}')
