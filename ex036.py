"""
Exercício Python 36: Escreva um programa para aprovar
o empréstimo bancário para a compra de uma casa. Pergunte
o valor da casa, o salário do comprador e em quantos
anos ele vai pagar.

A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.

"""
print('=+'*20)
print('Banco Rolos e Trambiques')
print('=+'*20)
print('\n')
valor_casa = float(input('Quanto custa a casa? R$').strip())
salario_mensal = float(input('Quanto você ganha por mês? R$ ').strip())
anos_pagamentos = int(input('Em quantos anos você quer pagar o imóvel? ').strip())

quantidade_meses = anos_pagamentos * 12
valor_prestacao = valor_casa / quantidade_meses
if valor_prestacao <= (salario_mensal * 30 / 100):
    print(f'Empréstimo liberado. O valor da prestação foi de R$ {valor_prestacao:.2f}')
else:
    print(f'Empréstimo NEGADO. O valor da prestação foi de R$ {valor_prestacao:.2f}')
