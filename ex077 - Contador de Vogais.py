"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
 deve mostrar, para cada palavra, quais são as suas vogais."""

tuple_names = ('Carro', 'Notredame', 'Java', 'Programação', 'Galinha',
               'desespero', 'Palavra', 'trabalhar', 'Cavalo', 'Caneta')

for palavra in tuple_names:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
