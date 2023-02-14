'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

rental_days = int(input('Quantos dias ficou alugado: '))
traveled_KM = float(input('Quantos KM rodados: '))

rental_days_price = rental_days * 60
traveled_KM_price = traveled_KM * 0.15

print(f'O total a pagar é de R${rental_days_price + traveled_KM_price:.2f}')