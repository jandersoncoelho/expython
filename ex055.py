"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.

"""
maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso informado foi {maior_peso:.2f}kg')
print(f'O menor peso informado foi {menor_peso:.2f}kg')
