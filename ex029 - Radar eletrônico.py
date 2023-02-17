'''Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
 dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

# Leitura da velocidade do carro
car_speed = float(input('Qual é a velocidade atual do carro? '))

# Calculo da Multa
traffic_ticket = (car_speed - 80) * 7

# Condicionais de velocidade
if car_speed <= 80:
    print('Tenha um bom dia, dirija com segurança!')
else:
    print('Você foi MULTADO!')
    print(f'Sua multa foi de R${traffic_ticket:.2f}')
    print('Dirija com MAIS segurança!')
