'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' Rod Store '))

# input da compra e das opção de pagamento
buy_value = float(input('Valor da compra: '))
option_payment = int(input('''Formas de pagamento:
[ 1 ] à Vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão
Qual a sua opção: '''))

# Condicionais
if option_payment == 1:
    print(f'Sua compra de R${buy_value:.2f} tem 10% de desconto e custará R${buy_value - (buy_value * 0.1):.2f}')
elif option_payment == 2:
    print(f'Sua compra de R${buy_value:.2f} tem 5% de desconto e custará R${buy_value - (buy_value * 0.05):.2f}')
elif option_payment == 3:
    print(f'Sua compra de R${buy_value} ficará em 2X de R${buy_value / 2:.2f}')
elif option_payment == 4:
   installments = int(input('Em quantas parcelas: '))
   amount_installment = buy_value + (buy_value * 0.2)
   print(f'Sua compra de {buy_value:.2f} vai custar R${amount_installment} em {installments}X de RS{amount_installment / installments:.2f}')
else:
    print('Opção inválida, tente novamente.')

