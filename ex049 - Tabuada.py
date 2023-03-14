'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

# Criação da variavel com input da tabuada
multiplication_table = int(input('Digite um número para ver a sua tabuada: '))

# Laço 'for' usando o número da tabuada
for c in range(1, 11):
    print(f'{multiplication_table} X {c:2} = {multiplication_table * c}')
