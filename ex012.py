"""
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.

"""
preço_produto = float(input('Informe o preço atual do produto: R$ '))
preço_com_desconto = preço_produto - (preço_produto * 0.05)
print('O novo preço com 5% de desconto é R${:.2f}.'.format(preço_com_desconto))
