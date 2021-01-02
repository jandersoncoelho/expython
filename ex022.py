"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

"""
nome_completo = str(input('Escreva o nome completo da pessoa:')).strip()
print(nome_completo.upper())
print(nome_completo.lower())
print('Quantidade de letras no nome: {}'.format(len(nome_completo)-nome_completo.count(' ')))
nome_dividido = nome_completo.split()


print('Seu primeiro nome é {} e a quantidade de letras no primeiro nome: {}'.format(nome_dividido[0], len(nome_dividido[0])))
