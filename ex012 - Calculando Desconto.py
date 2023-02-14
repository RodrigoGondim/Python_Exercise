'''Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

product_full_price = float(input('Qual é o preço do produto: R$'))
discount = 0.05
product_discount_price = product_full_price - (product_full_price * discount)
print(f'O produto que custa R${product_full_price:.2f} e tem um desconto de 5%, ficará custando R${product_discount_price:.2f}')