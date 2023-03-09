'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

# input
int_value = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
converter = int(input('Qual a sua opção: '))

# Comparativos + transformação e tratamento
if converter == 1:
    print(f'{int_value} convertido para BINÁRIO fica {bin(int_value)[2:]} ')
elif converter == 2:
    print(f'{int_value} convertido para OCTAL fica {oct(int_value)[2:]} ')
elif converter == 3 :
    print(f'{int_value} convertido para HEXADECINAL fica {hex(int_value)[2:]} ')
else:
    print('Opção Inválida. Tente novamente!')
