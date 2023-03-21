"""Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
 média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
 quer ou não continuar a digitar valores."""

# Váriaveis
pergunta = 'Sim'
count_number = sum_number = 0
smaller_number = bigger_number = 0

# Repetição while
while pergunta != 'N':
    int_number = int(input('Digite um valor: '))
    count_number += 1
    sum_number += int_number
    if count_number == 1:  # Condicionais do MENOR e MAIOR número
        smaller_number = int_number
        bigger_number = int_number
    else:
        if int_number < smaller_number:
            smaller_number = int_number
        elif int_number > bigger_number:
            bigger_number = int_number
    pergunta = str(input('Deseja Continuar? S/N ')).strip().upper()[0]  # Quebra do While - Break

# Impressões dos resultados petidos
print(f'Você digitou {count_number} números e sua média foi {sum_number / count_number}')
print(f'O menor número foi {smaller_number} e o maior foi {bigger_number}')
