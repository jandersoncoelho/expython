'''
Exercício Python 088: 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

- O programa vai perguntar quantos jogos serão gerados.
- vai sortear 6 números entre 1 e 60 para cada jogo.
- cadastre tudo em uma única lista composta.

'''
import random

lista_palpites = []
numero_palpites = int(input('Quantos palpites para Mega Sena você quer gerar? '))

for _ in range(numero_palpites):
    palpite = []
    cont = 0
    while True:
        dezena = random.choice(range(1, 60))
        if dezena not in palpite:
            palpite.append(dezena)
            cont += 1
        if cont >= 6:
            break
    palpite.sort()
    lista_palpites.append(palpite[:])

# Imprimindo a matriz
##print(lista_palpites)
print(f'\nA lista de {numero_palpites} jogos para apostar na Mega Sena é:')
print()
print('-' * 40)
for palpite in lista_palpites:
    print(palpite)
print('-' * 40)

