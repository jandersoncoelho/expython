'''
Exercício Python 094:

    - Crie um programa que leia nome, sexo e idade de várias pessoas

    - Guarde os dados de cada pessoa em um dicionário

    - Todos os dicionários devem estar em uma lista.

    - No final, mostre:

        A) Quantas pessoas foram cadastradas
        B) A média de idade
        C) Uma lista com as mulheres
        D) Uma lista de pessoas com idade acima da média

'''


lista_pessoas  = []
lista_mulheres = []
lista_acima_media = []
pessoa = {}
media_idade = soma_idade = 0

while True:
    pessoa.clear()
    nome_pessoa = input('Informe o nome: ')
    while True:
        sexo_pessoa = input('Informe o sexo (M -> Masclino) (F -> Feminino): ').upper()[0]
        if sexo_pessoa in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
        
    idade = int(input('Informe a idade: '))
    soma_idade += idade
    pessoa['nome'] = nome_pessoa
    pessoa['sexo_pessoa'] = sexo_pessoa.upper()
    pessoa['idade'] = idade
    
    if pessoa['sexo_pessoa'] == 'F':
        lista_mulheres.append(pessoa['nome'])

    lista_pessoas.append(pessoa.copy())
    while True:
        continuar = input('Deseja continuar o cadastro (S/N): ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    if continuar == 'N':
        media_idade = soma_idade / len(lista_pessoas)    
        break
    
print('-=' * 30)
print(lista_pessoas)
print('-=' * 30)
print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')
print(f'A média de idade das pessoas cadastradas é  {media_idade:.2f}.')
print('-=' * 30)

print('Lista de mulheres:')
for mulher in lista_mulheres:
    print(f'    - {mulher}')
print('-=' * 30)

print(f'Lista de pessoas com idade acima da média de {media_idade:.2f} anos:')
for pessoa in lista_pessoas:
    if (pessoa['idade'] >= media_idade):
        print(f'    - {pessoa["nome"]}')
print('-=' * 30)
