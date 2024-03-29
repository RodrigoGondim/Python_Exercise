"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
 indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
  não na tela o processo de cálculo do fatorial."""


def fatorial(num, show=False):
    """
    > Calcula o Fatorial de um número
    :param num: O número para ser calculado o Fatorial
    :param show: (Opcional) Mostra ou não o cálculo da multiplicação
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end=' ')
        f *= c
    return f


# Programa Principal
x = int(input('Fatorial: '))
print(fatorial(x, show=True))
