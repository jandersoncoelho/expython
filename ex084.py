"""

Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

"""
lista_pessoas = []
temp = []
maior_peso = menor_peso = 0

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(lista_pessoas) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        if temp[1] < menor_peso:
            menor_peso = temp[1]

    lista_pessoas.append(temp[:])
    temp.clear()
    resposta = input('Deseja continuar [S/N]: ').strip().upper()
    if resposta == 'N':
        break

print('+=' * 40)
print(f'A quantidade de pessoas cadastradas foi de {len(lista_pessoas)}.')

print('=' * 40)
print(f'Quantidade de pessoas cadastradas: {len(lista_pessoas)}')
print('=' * 40)

print(f'Pessoas mais pesadas com peso de {maior_peso}Kg:')

for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        print(f'Nome: {pessoa[0]}.')

print('=' * 40)
print(f'Pessoas mais leves com peso de {menor_peso}Kg:')

for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f'Nome: {pessoa[0]}.')
print('=' * 40)
