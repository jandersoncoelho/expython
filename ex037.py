"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""

print('=+'*20)
print('CONVERSOR DE BASES NUMÉRICAS')
print('=+'*20)
print('\n')
numero_inteiro = int(input('Informe o número inteiro: ').strip())
print('''Menu de opções:
1 - Para binário
2 - Para octal
3 - Para hexadecimal''')

controle_menu = int(input('Para qual base você deseja converter? '))

if controle_menu == 1:
    # print('{} convertido para binário é: {}'.format(numero_inteiro, bin(numero_inteiro)))
    print(f'{numero_inteiro} convertido para binário é: {numero_inteiro:b}')
elif controle_menu == 2:
    print(f'{numero_inteiro} convertido para octal é: {numero_inteiro:o}')
elif controle_menu == 3:
    print(f'{numero_inteiro} convertido para hexadecimal é: {numero_inteiro:#x}')
else:
    print(f'Ops! {controle_menu} não é uma opção válida!')
