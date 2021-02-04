"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

No Janken-pon, os jogadores devem simultaneamente esticar a mão,
na qual cada um formou um símbolo (que significa pedra, papel ou tesoura).
Então, os jogadores comparam os símbolos para decidir quem ganhou, da seguinte forma:

Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).

"""
from random import choice
from time import sleep
lista = ["Pedra", "Papel", "Tesoura"]
escolha_computador = choice(lista)
escolha_jogador = int(input('''
Faça sua escolha.
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura 
Opção: '''))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')
print('=-' * 40)
print(f'Computador escolheu {escolha_computador}')
if escolha_jogador == 1: #Pedra
    print('Usário escolheu Pedra.')
    print('=-' * 40)
    if escolha_computador == 'Pedra':
        print('Computador e usuário empataram')
    elif escolha_computador == 'Papel':
        print('Computador venceu.')
    elif escolha_computador == 'Tesoura':
        print('Usuário Venceu.')
elif escolha_jogador == 2: #Papel
    print('Usário escolheu Papel.')
    print('=-' * 40)
    if escolha_computador == 'Pedra':
        print('Computador venceu')
    elif escolha_computador == 'Papel':
        print('Computador e usuário empataram.')
    elif escolha_computador == 'Tesoura':
        print('Computador Venceu.')
elif escolha_jogador == 3: #Tesoura
    print('Usário escolheu Tesoura.')
    print('=-' * 40)
    if escolha_computador == 'Pedra':
        print('Computador venceu.')
    elif escolha_computador == 'Papel':
        print('Usuário venceu.')
    elif escolha_computador == 'Tesoura':
        print('Computador e usuário empataram.')
else:
    print('Opção inválida! Tente novamente.')
