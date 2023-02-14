'''Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento'''

your_salary = float(input('Quanto você ganha de salário: R$ '))
salary_increase = 0.15
new_salary = your_salary + (your_salary * salary_increase)
print(f'Seu salário de R${your_salary:.2f} com um aumento de {salary_increase * 100}% ficará R${new_salary:.2f}')