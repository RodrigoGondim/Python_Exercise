'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"'''

city_name = str(input('Digite o nome da cidade que você nasceu: ')).strip().lower()
print(city_name[:5] == 'santo')