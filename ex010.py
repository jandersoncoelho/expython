'''Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dólares ela pode comprar. '''

dinheiro_carteira = float(input('Informe quanto você tem na carteira: R$'))
cotacao_atual = float(input('Qual é a cotação do dólar hoje? '))
dinheiro_dolar = dinheiro_carteira / cotacao_atual
print('R${:.2f} em dólar: ${:.2f}'.format(dinheiro_carteira, dinheiro_dolar))
