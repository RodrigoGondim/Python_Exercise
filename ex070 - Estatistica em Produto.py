"""Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
 usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

# Contadores + While
your_bill = count_price_over_1000 = cheap_product_price = count = 0
cheap_product_name = ' '

while True:
    product_name = str(input('Nome do produto: '))
    product_price = float(input('Preço do produto: R$ '))
    count += 1
    if count == 1:  # Letra C
        cheap_product_price = product_price
        cheap_product_name = product_name
    else:
        if product_price < cheap_product_price:
            cheap_product_price = product_price
            cheap_product_name = product_name
    your_bill += product_price  # Letra A
    if product_price > 1000:  # Letra B
        count_price_over_1000 += 1
    option = ' '
    while option not in 'SN':
        option = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if option == 'N':
        break

# Respostas da letra 'A', 'B' e 'C'.
print(f'O total da sua compra foi de R$ {your_bill:.2f}')
print(f'Temos {count_price_over_1000} produto que custou mais de R$1000,00')
print(f'O produto mais barato foi {cheap_product_name} que custou R${cheap_product_price:.2f}')
