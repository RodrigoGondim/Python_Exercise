'''Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

celsius_temperature = float(input('Informe a temperatura em °C: '))
fahrenheit_temperature = (9 * celsius_temperature)  / 5 + 32
print(f'A temperatura de {celsius_temperature:.1f}°C convertidos para Fahrenheit são {fahrenheit_temperature:.1f}°F')