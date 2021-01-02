"""
Exercício Python 28: Escreva um programa que faça o computador
“pensar” em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
from random import randint
from time import sleep
print('-=-' * 10)
print('Jogo de Advinhação'.center(3, '='))
print('-=-' * 10)
numero_jogador = int(input('Advinha o número que eu estou pensando entre 0 e 5?: ').strip())
print('PROCESSANDO...')
sleep(3)
numero_computador = randint(0, 5)
if numero_jogador == numero_computador:
    print('Parabéns! Você advinhou! :)')
else:
    print('Ah não! Você perdeu! :( O número que eu pensei foi {} .'.format(numero_computador))
