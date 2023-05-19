"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

# Criação de Dict e List
soccer_player = dict()
gols = list()

# Inputs
soccer_player['Nome'] = str(input('Nome do Jogador(a): ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {soccer_player["Nome"]} jogou: '))

for c in range(1, partidas + 1):
    gols.append(int(input(f'    Quantos gols na {c}° partida: ')))


# Adicionando a lista dentro do Dict
soccer_player['Gols'] = gols[:]
soccer_player['Total de Gols'] = sum(gols)
print()
print('-=' * 30)

# Pritando bonito
print(soccer_player)
print()
print('-=' * 30)

for k, v in soccer_player.items():
    print(f'O "{k}" tem o valor "{v}"')
print()
print('-=' * 30)

print(f'O Jogador(a): {soccer_player["Nome"]} jogou {partidas} partidas')
for i, v in enumerate(soccer_player["Gols"]):
    print(f'     Na partida {i + 1}, fez {v} gols.')
print(f' Total de {soccer_player["Total de Gols"]} gols')
print()
print('-=' * 30)
