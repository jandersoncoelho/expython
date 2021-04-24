"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai
“pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.

"""
from random import randint
from time import sleep

print('-=-' * 10)
print('Jogo de Advinhação Versão 2.0'.center(3, '='))
print('-=-' * 10)
qtd_palpites = 0
numero_computador = randint(0, 10)
acertou = False
numero_jogador = int(input('Advinha o número que eu estou pensando entre 0 e 10?: ').strip())
while not acertou:
    if numero_jogador != numero_computador:
        acertou = False
        if numero_jogador < numero_computador:
            numero_jogador = int(input('Mais... Tente novamente: ').strip())
        elif numero_jogador > numero_computador:
            numero_jogador = int(input('Menos... Tente novamente: ').strip())
        qtd_palpites += 1
    else:
        acertou = True
print('Parabéns! Você advinhou! :)')
print(f'Você precisou de {qtd_palpites} para me vencer. O número que pensei foi {numero_computador}.')
