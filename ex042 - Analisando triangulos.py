'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

# Input das retas
side_1 = float(input('Primeiro segmento: '))
side_2 = float(input('Segundo segmento: '))
side_3 = float(input('Terceiro segmento: '))

# Condicionais
if side_1 < side_2 + side_3 and side_2 < side_1 + side_3:
    print(f'Os segmentos formam um triângulo do tipo:')
    # Tipo do triângulo
    if side_1 == side_2 == side_3:
        print('Equilátero')
    elif side_1 != side_2 != side_3 != side_1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos acima NÃO formam um triângulo.')
