"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

"""
num = int(input('Informe um número inteiro: ').strip())
cont = num
fatorial = 1
print(f'{num}! = {cont} ', end='')
while cont > 1:
    fatorial *= cont
    cont -= 1
    print(f'x {cont} ', end='')
print(f'= {fatorial}')
