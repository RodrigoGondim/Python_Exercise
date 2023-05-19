"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela."""

aluno = dict()
aluno['Nome'] = str(input('Nome do Aluno(a): ')).strip().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
else:
    aluno['Situação'] = 'RECUPERAÇÃO'
print('*' * 30)

for k, v in aluno.items():
    print(f' {k}: {v}')

