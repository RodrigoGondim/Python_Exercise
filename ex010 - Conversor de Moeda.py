'''Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
 ela pode comprar.'''
real = float(input('Quantos reais(R$) você tem na sua conta? RS'))
dollar = 5.18
print(f'Com {real:.2f} Reais você compra {real / dollar :.2f} Dolares')
