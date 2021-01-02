"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros

"""
print('=+'*20)
print('{:=^40}'.format(' VENDA DE PRODUTOS '))
print('=+'*20)
print('\n')
valor_produto = float(input('Informe o valor do produto: '))
forma_pagamento = int(input('''Formas de pagamento
1 - À vista dinheiro ou cheque: 10% de desconto
2 – à vista no cartão: 5% de desconto
3 – em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros 
Escolha a opção: '''))

if forma_pagamento == 1:
    preco_final = valor_produto - (valor_produto * 0.10)
    print(f'Valor total a pagar à vista com desconto de 10%: R${preco_final:.2f}.')
elif forma_pagamento == 2:
    preco_final = valor_produto - (valor_produto * 0.05)
    # print(f'Valor das parcelas: R${preco_final/2:.2f}.')
    print(f'Valor total a pagar à vista no cartão com 5% de desconto: R${preco_final:.2f}.')
elif forma_pagamento == 3:
    preco_final = valor_produto
    print(f'Valor das parcelas: R${preco_final / 2:.2f}.')
    print(f'Valor total a pagar à vista em até 2x no cartão: R${preco_final:.2f}.')
elif forma_pagamento == 4:
    qtd_parcelas = int(input('Informe a quantidade de parcelas:'.strip()))
    preco_final = valor_produto + (valor_produto * 0.20)
    print(f'Valor das parcelas: R${preco_final/qtd_parcelas:.2f}.')
    print(f'Valor total a pagar em {qtd_parcelas}x no cartão com 20% de juros: R${preco_final:.2f}.')

else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
