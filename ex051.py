"""
Exercício Python 51: Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.

"""
primeiro_termo = int(input('Informe o 1º termo da P.A.: ').strip())
razao = int(input('Informe a razão da P.A.: '))
ultimo_termo = primeiro_termo + (10 - 1) * razao
print(f'razão: {razao} e último termo: {ultimo_termo}.')
print('A progressão aritmética resultante será:')
for i in range(primeiro_termo, ultimo_termo + razao, razao):
    termo = primeiro_termo + (i - 1) * razao
    print(f'{i}', end=' -> ')
print('ACABOU.', end='')

