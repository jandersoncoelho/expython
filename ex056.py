"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade
e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

"""
soma_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
qtd_mulheres = 0
for p in range(1, 5):
    nome = input(f'Infome o nome da {p}ª pessoa: ')
    idade = int(input('Informe a sua idade: ').strip())
    sexo = input('Informe F se for mulher ou M se for homem: ').upper()
    soma_idade += idade
    if p == 1 and sexo == 'M':
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    if sexo == 'M' and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    if sexo == 'F' and idade < 20:
        qtd_mulheres += 1

media_idade = soma_idade / 4
print(f'A média das idades informadas é de {media_idade:.2f} anos.')
print(f'{nome_homem_mais_velho} é o homem mais velho de todos com {idade_homem_mais_velho} anos de idade.')
print(f'Há {qtd_mulheres} mulheres com menos de 20 anos.')
