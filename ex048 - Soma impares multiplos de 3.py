'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

# Criação de um contador e de um somador
count = sum = 0

# Laço 'for' dentro do intervalo pedido
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        sum += c
print(f'A soma dos {count} números que são ímpares e multiplos de 3, tem sua soma no valor de {sum}')