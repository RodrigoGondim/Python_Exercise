"""Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*num, sit=False):
    """
    > Function para analisar notas e situação de vários alunos.
    :param num: Uma ou Várias notas de alunos
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação geral
    :return: Um dicionário com várias informações sobre a turma
    """
    boletim = dict()
    boletim['Total'] = len(num)
    boletim['Maior Nota'] = max(num)
    boletim['Menor Nota'] = min(num)
    boletim['Média'] = sum(num) / len(num)
    if sit:
        if boletim['Média'] >= 7:
            boletim['Situação'] = 'BOA'
        elif boletim['Média'] >= 5:
            boletim['Situação'] = 'MÉDIA'
        else:
            boletim['Situação'] = 'RUIM'

    return boletim


# Programa principal
x = notas(7, 4, 5.5, 8, sit=True)
print(x)
help(notas)
