"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for
ímpar, desconsidere-o.

"""
soma_par = 0
for c in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma_par += num
print(f'A soma de apenas os números pares é: {soma_par}')
