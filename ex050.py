"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for
ímpar, desconsidere-o.

"""
soma_par = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro: '))
    if num % 2 == 0:
        cont += 1
        soma_par += num
print(f'A soma de apenas os {cont} números pares é: {soma_par}')
