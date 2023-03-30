"""Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
 digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. """

# Importação do sleep apenas para Firula
from time import sleep

while True:
    int_number = int(input('Digite um número para ver sua tabuada: '))
    if int_number < 0:  # Número NEGATIVO para o Break
        break
    for c in range(1, 11):
        print(f'{int_number} X {c:>2} = {c * int_number:>2}')
    print('-' * 40)
    sleep(1)  # Dentro do Loop

sleep(1)  # Fora do Loop
print('Programa de tabuada ENCERRADO! Volte Sempre :)')
