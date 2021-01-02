"""
Exercício Python 25:

Crie um programa que leia o
nome de uma pessoa e diga se ela tem “SILVA” no nome.

"""
nome = str(input('Informe o nome ')).strip().upper()
print('Contém "SILVA" nome? {}'.format('SILVA' in nome.upper()))
