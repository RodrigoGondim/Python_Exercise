'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

# Input do nome + tratamento de String
name = str(input('Digite uma frase: ')).strip().upper()
name_split = name.split()
name_together = ''.join(name_split)
name_reverse = ''
# Opção1: Ler a variavel de tras para frente > name_reverse = name_together[::-1]
# Opção2: Usando o 'for' para adicionar em uma variavel
for c in range(len(name_together) - 1, -1, -1):
    name_reverse += name_together[c]

# Condicional se é Palíndromo ou não
if name_together == name_reverse:
    print(f'A frase {name_together} é um PALÍNDROMO')
else:
    print(f'A frase {name_together} NÃO é um Palíndromo')
