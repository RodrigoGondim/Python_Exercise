"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior."""

from random import randint


def raffle(*num):
    for c in range(1, 6):
        numeros.append(randint(0, 10))
    print(f'Sorteando 5 números: {numeros}')


def soma_par():
    count = 0
    for value in numeros:
        if value % 2 == 0:
            count += value
    print(f'A soma dos valores Pares é igual a {count}')


numeros = []
raffle()
soma_par()
