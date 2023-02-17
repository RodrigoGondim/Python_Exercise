'''Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

# Input das retas
side_1 = float(input('Primeiro segmento: '))
side_2 = float(input('Primeiro segmento: '))
side_3 = float(input('Primeiro segmento: '))

# Condicionais
if side_1 < side_2 + side_3 and side_2 < side_1 + side_3:
    print(f'Os segmentos formam um triângulo.')
else:
    print('Os segmentos acima NÃO formam um triângulo.')