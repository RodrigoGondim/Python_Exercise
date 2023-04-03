"""Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense. Como em 2023 o Chapecoense não está na tabela o time será o CEARÁ"""

# Importação para firula
from time import sleep

# Lista de times em Mar/2023
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Athletico-PR', 'Atlético - MG',
         'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')

count = 1
print('A lista dos times de 2023 é: ')
for c in times:
    print(f'{count}° {c}')
    count += 1
    sleep(0.3)
print('=' * 120)

# Letra A
print(f'Os 5 primeiros colocados são {times[0:5]}')

# Letra B
print(f'Os 4 últimos colocados são {times[-4:]}')

# Letra D
print(f'O time do Ceará está na posição {times.index("Ceará") +1}°')
print('=' * 120)

# Letra C
print(f'Os times em ordem alfabética fica: ')
for c in sorted(times):
    print(c, end=', ')
    sleep(0.3)
