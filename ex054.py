"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de
sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maior idade e quantas já são maiores.

"""
from datetime import date
from typing import List

data_atual = date.today()
ano_atual = data_atual.year
ano_nasc: List[int] = []
for c in range(1, 8):
    ano_nasc.append(int(input(f'Informe o ano de nascimento da {c}ª pessoa: ').strip()))
print(ano_nasc)
qtd_maior_idade = 0
qtd_menor_idade = 0
for i in ano_nasc:
    idade = ano_atual - int(i)
    if idade >= 0:
        if idade < 18:
            qtd_menor_idade += 1
        elif idade > 18:
            qtd_maior_idade += 1
print(f'Total de pessoas com menos de 18 anos: {qtd_menor_idade}.')
print(f'Total de pessoas com mais de 18 anos: {qtd_maior_idade}.')
