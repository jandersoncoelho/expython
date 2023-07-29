'''
Exercício Python 091:

- Crie um programa onde 4 jogadores joguem um dado.

- A regra do jogo é que cada jogador tenha resultados aleatórios.

- Guarde esses resultados em um dicionário em Python.

- No final, coloque esse dicionário em ordem decrescente.

- O vencedor tirou o maior número no dado.

- Exemplo de interface com o usuário:

"
Jogador 1: tirou 4.
Jogador 2: tirou 1.
Jogador 3: tirou 6.
Jogador 4: tirou 2.
"
- Exemplo de saída:

"
====== RANKING DOS JOGADORES ======

1º Lugar: Jogador 3: tirou 6.
2º Lugar: Jogador 1: tirou 4.
3º Lugar: Jogador 4: tirou 2.
4º Lugar: Jogador 2: tirou 1.

-----------------------
     << VENCEDOR >>
-----------------------

     Jogador 3


"
'''

from random import randint
from time import sleep
from operator import itemgetter

sorteio = []

for j in range(1, 5):
    dado = {}
    dado['jogador'] = f'Jogador {j}'
    dado['jogada'] = randint(1, 6)
    sorteio.append(dado)

for i, dado in enumerate(sorteio):
    print(f"O {dado['jogador']} jogou {dado['jogada']}.")
    sleep(1)

print('')

sorteio = sorted(sorteio, key=lambda dado: dado['jogada'], reverse=True)
##sorteio = sorted(dado.items(), key=itemgetter(1), reverse=True)

print("====== RANKING DOS JOGADORES ======\n")

for i, dado in enumerate(sorteio):
    print(f"{i + 1}º Lugar: {dado['jogador']}: tirou {dado['jogada']}.")
    sleep(1)
print('')
print("-" * 26)
print(" << VENCEDOR >>".center(26))
print("-" * 26)
print(f"{sorteio[0]['jogador'].center(26)}\n")
