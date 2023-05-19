"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente."""


def ficha(name='<Desconhecido>', gol=0):
    """
    > Exercício para treinar parametros OPCIONAIS.
    :param name: Nome do jogador
    :param gol: número de gols marcados
    :return: Retorna um print relacionando o nome e quant de gols
    """
    print(f'O jogador {name} fez {gol} gol(s) na partida.')


# Programa Principal
player_name = str(input('Nome do jogador: ')).strip()
score = str(input('Número de gols: '))

# 'Validando' o gol
if score.isnumeric():
    score = int(score)
else:
    score = 0
# 'Validando' o nome
if player_name.strip() == '':
    ficha(gol=score)
else:
    ficha(player_name, score)


