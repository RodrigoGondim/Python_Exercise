'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

number_int_analyze = int(input('Digite um número de 0 a 9999: '))
u = number_int_analyze // 1 % 10
d = number_int_analyze // 10 % 10
c = number_int_analyze // 100 % 10
m = number_int_analyze // 1000 % 10

print(f'Unidade {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')