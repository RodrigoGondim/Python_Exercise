"""Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador."""

from time import sleep

# Criação de Dict e List
soccer_player = dict()
gols = list()
team = list()
while True:
    # Inputs
    soccer_player.clear()
    soccer_player['Nome'] = str(input('Nome do Jogador(a): ')).strip().capitalize()
    count = int(input(f'Quantas partidas {soccer_player["Nome"]} jogou: '))
    gols.clear()
    for c in range(1, count + 1):
        gols.append(int(input(f'    Quantos gols na {c}° partida: ')))
    # Adicionando a lista dentro do Dict
    soccer_player['Gols'] = gols[:]
    soccer_player['Total de Gols'] = sum(gols)
    team.append(soccer_player.copy())
    while True:
        option = str(input('Continuar[S/N]: ')).upper()[0]
        if option in 'SN':
            break
        print('ERRO! Responda S/N')
        print('-=' * 30)
        sleep(1)
    if option == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in soccer_player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Monstar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(team):
        print(f'ERRO! Não existe jogar com código {busca}')
    else:
        print(f' ---LEVANTAMENTO DO JOGADOR {team[busca]["Nome"]}:')
        for i, g in enumerate(team[busca]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 40)
print('FIM')
