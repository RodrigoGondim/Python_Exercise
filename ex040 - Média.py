'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

# Inputs da questão 007
studentgrade_1st = float(input('Primeira nota: '))
studentgrade_2st = float(input('Segunda nota: '))
student_average = (studentgrade_1st + studentgrade_2st) / 2

# Condicionais

if student_average < 5.0:
    print('Reprovado')
elif 5.0 < student_average < 6.9:
    print('Recuperação')
else:
    print('Aprovado')


