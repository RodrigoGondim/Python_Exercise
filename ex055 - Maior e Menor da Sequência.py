"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lidos."""

# Contadores
lower_weight = greater_weight = 0

# Repetição 'for'
for c in range(1, 6):
    weight = float(input(f'Peso da {c}° Pessoa: '))
    if c == 1:
        lower_weight = weight
        greater_weight = weight
    else:
        if weight < lower_weight:
            lower_weight = weight
        if weight > greater_weight:
            greater_weight = weight

# Print do Menor e do Maior peso
print(f'O menor peso foi de {lower_weight:.2f}Kg')
print(f'O maior peso foi de {greater_weight:.2f}Kg')
