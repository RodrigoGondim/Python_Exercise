'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas'''

# Distância da viagem
trip_distance = float(input('Qual a distância da sua viagem: '))

# Calculos + Condicionais
short_trip_price = trip_distance * 0.5
long_trip_price = trip_distance * 0.45

if trip_distance <= 200:
    print(f'Você está preste a começar uma viagem de {trip_distance} Km.')
    print(f'E sua passagem será de R${short_trip_price:.2f}')
else: # trip_distance >= 200:
    print(f'Você está preste a começar uma viagem de {trip_distance} Km.')
    print(f'E sua passagem será de R${long_trip_price:.2f}')