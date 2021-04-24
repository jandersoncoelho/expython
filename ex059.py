"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""

print('-=-' * 20)
print('CALCULADORA COM 2 NÚMEROS INFORMADOS'.center(60, '='))
print('-=-' * 20)
n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
opção = 0
while opção != 5:
    print('-=-' * 20)
    print('MENU DE OPÇÕES'.center(60, ' '))
    # print('-'.center(60) * 20)

    print('''
        1 - somar
        2 - multiplicar
        3 - maior
        4 - calcular novos números
        5 - sair
    '''.center(100, ' '))
    opção = int(input('Escolha uma das opções exibidas: ').strip())
    print('-=-' * 20)
    if 1 <= opção <= 5:
        if opção == 1:
            print(f'A soma entre {n1} e {n2} é {n1 + n2}'.center(60, ' '))
        elif opção == 2:
            print(f'O produto entre {n1} e {n2} é {n1 * n2}'.center(60, ' '))
        elif opção == 3:
            if n1 > n2:
                print(f'{n1} é maior.'.center(60, ' '))
            elif n2 > n1:
                print(f'{n2} é maior.'.center(60, ' '))
            else:
                print('Os números informados são iguais.')
        elif opção == 4:
            n1 = int(input('Digite o primeiro valor inteiro: '))
            n2 = int(input('Digite o segundo valor inteiro: '))
        elif opção == 5:
            opção = 5
        # print('-=-' * 20)
    else:
        print(' Ooops! opção inválida! '.center(60, '-'))

