'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
 da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
  o empréstimo será negado.'''

# Input do Valor da casa, Salário e tempo
buyer_salary = float(input('Qual o seu salário: R$'))
property_value = float(input('Qual o valor do imóvel: R$'))
years_of_funding = int((input('Quanto anos de financiamento: ')))
provision = property_value / (years_of_funding * 12)
print(f'Pagar pagar um imóvel de R${property_value:.2f} em {years_of_funding} anos ou {years_of_funding * 12} meses.')
print(f'A prestação será de R${provision:.2f}')

# Emprestimo aceito/negado
if provision <= (buyer_salary * 0.3):
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo Negado!')
