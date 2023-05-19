"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
 aluno individualmente."""

register = list()
while True:
    name = str(input('Nome do aluno(a): '))
    grade_1 = float(input('Nota 1: '))
    grade_2 = float(input('Nota 2: '))
    avarage = (grade_1 + grade_2) / 2
    register.append([name, [grade_1, grade_2], avarage])
    question = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    if question in 'Nn':
        break
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
print('-' * 30)

for i, a in enumerate(register):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Deseja ver qual aluno?(999 para parar): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(register) - 1:
        print(f'Notas de {register[opc][0]} são {register[opc][1]}')
print('Volte SEMPRE')
