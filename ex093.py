'''

Exercício Python 093:

- Crie um programa que gerencie o aproveitamento de um jogador de futebol.

- O programa vai ler o nome do jogador e quantas partidas ele jogou.

- Depois vai ler a quantidade de gols feitos em cada partida.

- No final, tudo isso será guardado em um dicionário, incluindo o total
  de gols feitos durante o campeonato.


'''

jogador = dict()
partidas = list()
    
nome_jogador = str(input('Informe o nome do jogador: '))
num_partidas = int(input(f'Informe o número de partidas do jogador {nome_jogador}: '))

for partida in range(1, num_partidas + 1):
    partidas.append(int(input(f'    Quantos gols feitos na {partida}ª? ')))


jogador['nome_jogador'] = nome_jogador
jogador['total_partidas'] = sum(partidas)
jogador['partidas'] = partidas[:]

print('*' * 60)   
print(jogador)
