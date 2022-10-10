'''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


'''


print('-=' * 30)
print('SOMA DE VÁRIOS NÚMEROS INTEIROS'.center(60))
print('-=' * 30)

qtd_inteiros = 0
soma_inteiros = 0
numero_informado = int(
    input('Digite um número inteiro [999 para parar]: ').strip())

while numero_informado != 999:
    qtd_inteiros = qtd_inteiros + 1
    soma_inteiros = soma_inteiros + numero_informado
    numero_informado = int(
        input('Digite um número inteiro [999 para parar]:').strip())

print('-=' * 30)
print(f'TOTAL DE NÚMEROS INTEIROS INFORMADOS: {qtd_inteiros}'.center(60))
print(f'SOMA TOTAL DE NÚMEROS INTEIROS: {soma_inteiros}'.center(60))
print('-=' * 30)
