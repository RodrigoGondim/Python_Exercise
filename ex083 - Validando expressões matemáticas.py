"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

# Input da expressão e criação da lista
expr = str(input('Digite uma expressão: '))
stack = []

# Para cada '(' add +1 a lista e para cada ')' remove -1 da lista
for char in expr:
    if char == '(':
        stack.append('(')
    elif char == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

# Print se é válida ou ínvalida
if len(stack) == 0:
    print('Sua expressão é VÁLIDA!')
else:
    print('Sua expressão é ÍNVALIDA')
