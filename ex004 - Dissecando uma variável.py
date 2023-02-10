'''Ex004 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

word_to_analysis = input('Digite algo para ser analisado: ')
print('Só tem espaço?',word_to_analysis.isspace())
print('É um número? ',word_to_analysis.isnumeric())
print('É um albético?',word_to_analysis.isalpha())
print('É alfanumerico?',word_to_analysis.isalnum())
print('Éstá em maiúscula?',word_to_analysis.islower())
print('Está em minúscula? ',word_to_analysis.isupper())