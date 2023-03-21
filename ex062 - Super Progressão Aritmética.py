"""Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

# Inputs + Contadores
print('Gerador de PA')
print('*=' * 15)
first_term = int(input('Primeiro termo: '))
between_term = int(input('Razão: '))
termo = first_term
count = 1
more = 10
total = 0

# Repetição while dentro de while
while more != 0:
    total += more
    while count <= total:
        print(f'{termo}', end=' ')
        termo += between_term
        count += 1
    more = int(input('\nQuantos termos a mais você que ver? '))
print(f'Finalizando com {total} termos mostrados')
