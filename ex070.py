'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

'''
total_gasto = 0
qtd_que_mil = 0
mais_que_mil = 0
cont = 0
menor_preco = 0
desc_produto_menor = ''

while True:
    desc_produto = str(input('Decrição do produto: ').strip().upper())
    preco_produto = float(input('Preço: R$').strip())
    cont += 1
    total_gasto += preco_produto

    if preco_produto > 1000:
        qtd_que_mil += 1

    if cont == 1 or preco_produto < menor_preco:
        menor_preco = preco_produto
        desc_produto_menor = desc_produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ').strip().upper())[0]
    if continuar == 'N':
        break

print('{:-^40}'.format(' RESUMO DA COMPRA '))
print(f'O total gasto na compra foi R$ {total_gasto:.2f}.'.replace('.', ','))
print(
    f'A quantidade de produtos que custam mais que R$1000,00 é {qtd_que_mil}.')
print(
    f'O produto mais barato foi {desc_produto_menor} que custou R${menor_preco:.2f}.')
print('{:-^40}'.format(''))
