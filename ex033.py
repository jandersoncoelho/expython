"""
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""
n1 = int(input('Digite o primeiro número: ').strip())
n2 = int(input('Digite o segundo número: ').strip())
n3 = int(input('Digite o terceiro número: ').strip())
maior = 0
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print('{} é o maior número'.format(maior))

menor = 0
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print(f"{menor} é o menor número")
