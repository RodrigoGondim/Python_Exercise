'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

# input do salário
your_salary = float(input('Digite seu salário: R$'))
salary_increase = 0
# Condicionais
if your_salary > 1250.00:
    salary_increase = 0.10
    print(f'Seu salário de R${your_salary:.2f} passou a ser de R${your_salary + (your_salary * salary_increase):.2f}')
if your_salary <= 1250.00:
    salary_increase = 0.15
    print(f'Seu salário de R${your_salary:.2f} passou a ser de R${your_salary + (your_salary * salary_increase):.2f}')
