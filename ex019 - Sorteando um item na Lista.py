'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice
students_1 = str(input('Nome do primeiro aluno: '))
students_2 = str(input('Nome do segundo aluno: '))
students_3 = str(input('Nome do terceiro aluno: '))
students_4 = str(input('Nome do quarto aluno: '))


list_students = [students_1, students_2, students_3, students_3, students_4]
chosen_student = choice(list_students)

print(f'O aluno(a) sorteado(a) foi: {chosen_student}')

