"""
Exercício Python 30: Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR.

"""
numero = int(input('Digite um número inteiro: ').strip())
if numero % 2 == 0:
    print('Número par')
else:
    print('Número ímpar.')