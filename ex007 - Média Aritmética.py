'''Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

studentsname = str(input('Nome do(a) aluno(a): '))
studentgrade_1st = float(input('Primeira nota: '))
studentgrade_2st = float(input('Segunda nota: '))
student_average = (studentgrade_1st + studentgrade_2st) / 2
print(f'''O(a) Aluno(a): {studentsname},
Na primeira avaliação tirou nota {studentgrade_1st}
Na segunda avaliação tirou {studentgrade_2st}
E teve uma média de {student_average}''')
