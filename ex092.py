'''

Exercício Python 092:

- Crie um programa que leia nome, ano de nascimento e carteira de trabalho.

- Cadastre-o (com idade) em um dicionário.

- Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o
  ano de contratação e o salário.

- Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
  aposentar.

'''
from datetime import date

pessoa = {}
pessoa['nome'] = str(input('Informe o nome: '))
pessoa['ano_nascimento'] = int(input('Informe o ano de nascimento: '))
pessoa['idade'] = date.today().year - pessoa['ano_nascimento']
pessoa['num_ctps'] = int(input('Informe o número da CTPS. Informe 0 se não tiver: '))
if (pessoa['num_ctps'] != 0):
    pessoa['ano_contratacao'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe o salário: '))
    pessoa['idade_aposentadoria'] = pessoa['idade'] + ((pessoa['ano_contratacao'] + 35) - date.today().year)
print('-=' * 40)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
