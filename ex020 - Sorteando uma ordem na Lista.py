'''Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
students_1 = str(input('Nome do primeiro aluno: '))
students_2 = str(input('Nome do segundo aluno: '))
students_3 = str(input('Nome do terceiro aluno: '))
students_4 = str(input('Nome do quarto aluno: '))

list_students = [students_1, students_2, students_3, students_4]
shuffle(list_students)

print(f'A ordem de apresentação será: {list_students}')
