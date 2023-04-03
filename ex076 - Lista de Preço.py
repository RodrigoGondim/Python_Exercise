"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

# 'Lista' de material escolar
school_supplies_name_price = ('Lápis', 1.99, 'Caderno', 35, 'Estojo', 19.99, 'Borracha', 3, 'Mochila', 149.99, 'Caneta',
                              2.99, 'Lápis de cor', 49.99)

# Firula para deixar bonito
print('-' * 40)
print(f'{"Lista de Preços":^40}')
print('-' * 40)

# 'For' para poder separar o ‘Item’ do Preço e organizar numa tabela para melhorar o visual
for c in range(len(school_supplies_name_price)):
    if c % 2 == 0:
        print(f'{school_supplies_name_price[c]:.<30}', end='')
    else:
        print(f'R${school_supplies_name_price[c]:>7.2f}')
