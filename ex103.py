'''

Exercício Python 103:

- Faça um programa que tenha uma função chamada ficha().
- Ela receberá dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
- O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
- Crie "docstrings" para quando o usuário digitar a função "help()" saiba como utilizá-la.
- Escreva o código usando a "PEP8" e o "Zen to Python".

'''


def ficha(nome_jogador='<desconhecido>', quantidade_gols=None):
    if quantidade_gols.isnumeric():
        return nome_jogador, quantidade_gols
    else:
        return nome_jogador, quantidade_gols

    # return nome_jogador, gols_jogador


# Programa Principal
nome = str(input('Informe o nome do jogador: '))
gols = str(input('Informe a quantidade de gols: '))

ficha_jogador = ficha(nome_jogador=nome, quantidade_gols=gols)

print(f'O jogador {ficha_jogador[0]}, fez {ficha_jogador[1]} gols.')