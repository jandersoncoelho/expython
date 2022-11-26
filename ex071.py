'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

-> TESTE DE PROGRAMA

531
500+20+10+1
10-> 50,00
1 -> 20,00
1 -> 10,00
1 -> 1,00

'''
import math

notas_cinquenta = notas_vinte = notas_dez = notas_um = 0

while True:
    print('=' * 40)
    print('{:-^40}'.format('BANCO CURSO EM VÍDEO'))
    print('=' * 40)

    valor_sacado = int(input('Informe o valor a ser sacado: R$').strip())
    notas_cinquenta = math.trunc(valor_sacado / 50)
    notas_vinte = math.trunc((valor_sacado % 50) / 20)
    notas_dez = math.trunc((valor_sacado % 20) / 10)
    notas_um = math.trunc((valor_sacado % 10) / 1)

    continuar = ' '
    while continuar not in 'SN':
        print(f'Notas de R$50,00: {notas_cinquenta}')
        print(f'Notas de R$20,00: {notas_vinte}')
        print(f'Notas de R$10,00: {notas_dez}')
        print(f'Notas de R$1,00: {notas_um}')
        print(f'O valor sacado pelo usuário foi de R${valor_sacado},00')
        continuar = str(input('Deseja continuar [S/N]: ').strip().upper())[0]
    if continuar == 'N':
        break
print('=' * 40)
print('{:-^40}'.format('VOLTE SEMPRE!'))
print('=' * 40)
