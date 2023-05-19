"""Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
 parâmetro e mostre uma mensagem com tamanho adaptável."""


def escreva(txt):
    word_size = len(txt) + 4
    print('~' * word_size)
    print(f'  {txt}')
    print('~' * word_size)


escreva('Python')
print()
escreva('Hello world')
print()
escreva('Dev em Python')
