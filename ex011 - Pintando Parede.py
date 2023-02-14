'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
 quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

width = float(input('Qual a largura da parede: '))
height = float(input('Qual a altura da parede: '))
area = width * width
paint = area / 2

print(f'Sua parede de medidas {width:.2f} X {height:.2f} tem {area:.2f}² de área')
print(f'Para pintar a sua parede de {area:.2f}m², você vai precisar de {paint} Litros de tinta')