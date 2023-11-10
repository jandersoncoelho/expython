'''

Exercício Python 103:

- Faça um programa que tenha uma função chamada ficha().
- Ela receberá dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
- O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
- Crie "docstrings" para quando o usuário digitar a função "help()" saiba como utilizá-la.
- Escreva o código usando a "PEP8" e o "Zen to Python".

'''


def ficha(nome_jogador='<desconhecido>', quantidade_gols=None):
    restult_ficha = []
    if quantidade_gols.isnumeric():
        restult_ficha.append(quantidade_gols)
    else:
        restult_ficha.append(0)
    if nome_jogador.strip() != '':
        restult_ficha.append(nome_jogador)
    else:
        restult_ficha.append('<desconhecido>')

    return restult_ficha


# Programa Principal
nome = str(input('Informe o nome do jogador: '))
gols = str(input('Informe a quantidade de gols: '))

ficha_jogador = ficha(nome, gols)

print(f'O jogador {ficha_jogador[1]}, fez {ficha_jogador[0]} gols.')