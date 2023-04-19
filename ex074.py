'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

'''

import random

# Gerando cinco números aleatórios e colocando em uma tupla
tupla_numeros = tuple(random.sample(range(0, 9), 5))

# Mostrando a listagem de números gerados
print(f"Os números gerados foram: {tupla_numeros}")

# Indicando o menor e o maior valor na tupla
print(f"O menor valor é: {min(tupla_numeros)}")
print(f"O maior valor é: {max(tupla_numeros)}")
