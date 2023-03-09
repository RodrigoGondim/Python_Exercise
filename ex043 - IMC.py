'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

# Input do peso e altura
weight = float(input('Qual o seu peso (Kg): '))
height = float(input('Qual a sua altura (m): '))

# Calculando o IMC
imc = weight / (height ** 2)

# Condicionais do IMC
if imc < 18.5:
    print('A pessoa está: Abaixo do Peso ')
elif 18.5 <= imc < 25:
    print('A pessoa está: No Peso Ideal')
elif 25 <= imc < 30:
    print('A pessoa está: Com Sobrepeso')
elif 30 <= imc < 40:
    print('A pessoa está: Com Obesidade ')
else:
    print('A pessoa está: Com Obesidade Mórbida ')

print(imc)
