'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8


'''


print('Sequência de Fionacci', end='\n')
print('-=' * 10)

num_termos = int(
    input('Informe a quantidade de termos da sequência: ').strip())
termo_anterior = 1
proximo_termo = 0
cont = 0
while cont < num_termos:

    print(termo_anterior, end=', ')
    # termo_sequencia = 1
    termo_sequencia = termo_anterior + proximo_termo
    proximo_termo = termo_anterior
    termo_anterior = termo_sequencia
    cont += 1

print('\nacabou')
