"""
Exercício Python 52: Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo.

"""
num = int(input('Digite um número inteiro: ').strip())
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[0:31m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} é divisível {tot} vezes.')
if tot == 2:
    print(f'O número {num} é PRIMO.')
else:
    print(f'O número {num} NÃO é PRIMO.')
