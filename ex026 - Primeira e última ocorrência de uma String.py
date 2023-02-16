'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

# Input da frase e tratamento
name_analyse = str(input('Digite uma frase: ')).strip().upper()

# Contador de letra 'A'
letter_counter_a = name_analyse.count('A')
print(f'A frase {name_analyse} tem {letter_counter_a} letras A.')

# Posição que a letra 'A' aparece pela 1° vez
print(f'A letra A aparece a 1° vez na posição {name_analyse.find("A")+1}')

# Posição que a letra 'A' aparece pela última vez
print(f'A letra A aparece pela última vez na posição {name_analyse.rfind("A")+1}')
