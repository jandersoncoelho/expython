'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

'''
while True:
    num = int(
        input('Informe um número inteiro que você deseja ver a tabuada (Digite um número negativo para sair do programa): ').strip())

    print('='*12)
    if num < 0:
        break

    print(f'A tabuada de {num} é:')
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('=' * 12)

print('FIM')
