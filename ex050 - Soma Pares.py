'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

# Criação do contador e somador
sum_pair = count_pair = 0
for c in range(1, 7):
    int_num = int(input(f'Digite o {c}°: '))
    if int_num % 2 == 0: # Apenas contar e somar SE for PAR
        sum_pair += int_num
        count_pair += 1
print(f'Foram digitados {count_pair} números pares e sua soma é de {sum_pair}')