'''Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros'''
measure_meters = float(input('Quantos metros você quer converter: '))
kilometers = measure_meters / 1000
centimeters = measure_meters * 100
millimeter = measure_meters * 1000

print(f'A conversão de {measure_meters} metros são {kilometers}Km, {centimeters} cm, {millimeter} mm')
