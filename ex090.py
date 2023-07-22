'''
Exercício Python 090:

- Faça um programa que leia nome e média de um aluno.

- Se a média for menor que 6, Coloque a situação como "Reprovado",
  caso seja maior que 6 coloque "Aprovado".

- Guarde as informações fornecidas e o resultado em um dicionário.

- No final, mostre o conteúdo da estrutura na tela.

'''
aluno = {}

aluno['nome'] = input('Nome do aluno: ')
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))

if aluno['média'] >= 6:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-' * 30)
for chave, valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')
print('-' * 30)

