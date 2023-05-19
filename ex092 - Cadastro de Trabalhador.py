"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

# Importações
from datetime import datetime

# Criação do Dict vazio
worker = dict()

# Add informações ao Dicionário
worker['Nome'] = str(input('Nome do trabalhador(a): ')).strip().capitalize()
worker['Nascimento'] = int(input('Ano do nascimento: '))
worker['Idade'] = datetime.now().year - worker['Nascimento']
worker["CTPS"] = int(input('Número da carteira de trabalho (0 para não tem): '))
if worker['CTPS'] != 0:
    worker['Contratação'] = int(input('Ano da contratação: '))
    worker['Salário'] = float(input('Salário: R$'))
    worker['Aposentadoria'] = worker['Idade'] + ((worker['Contratação'] + 35) - datetime.now().year)

# Printando bonito
for k, v in worker.items():
    print(f'`{k}: {v}')
