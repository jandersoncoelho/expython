'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''
import random
import time


quant_vitorias = 0
while True:
    numero_jogador = 0
    numero_computador = random.randrange(1, 10)
    soma_numeros = 0

    print('-=' * 30)
    print(' - JOGO DO PAR OU ÍMPAR - '.center(60, ' '))
    print('-=' * 30)

    print('--' * 30)
    print(' -> MENU <- '.center(60, ' '))
    print('1 - PAR')
    print('2 - ÍMPAR')
    print('--' * 30)

    escolha = int(
        input('Escolha uma opção: ').strip())

    if (escolha in (1, 2)):

        numero_jogador = int(
            input('Escolha um número: ').strip())

        if (numero_jogador in range(1, 11)):

            soma_numeros = numero_jogador + numero_computador

            print(
                f'Jogador: {numero_jogador} , Computador: {numero_computador}')

            if (escolha == 1 and (soma_numeros % 2 == 0)):

                print(
                    f'Viva Você venceu! A soma dos resultados deu {soma_numeros} e é PAR')
                quant_vitorias += 1
                time.sleep(2)
            elif (escolha == 2 and (soma_numeros % 2 != 0)):

                print(
                    f'Viva Você venceu! A soma dos resultados deu {soma_numeros} e é ÍMPAR')
                quant_vitorias += 1
                time.sleep(2)

            else:

                print(
                    f'Que pena o computador ganhou! A soma dos resultados deu {soma_numeros}.')
                print(
                    f'Quantidade de vitórias consecutivas do jogador: {quant_vitorias}')
                time.sleep(2)
                break
        else:
            print('JOGADA INVÁLIDA: TEM QUE SER ENTRE 1 E 10!!')
            time.sleep(2)

    else:
        print('OPÇÃO INVÁLIDA: TEM QUE SER ENTRE 1 E 2!!')
        time.sleep(2)
