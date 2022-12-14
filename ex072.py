'''
Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''
numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
                   'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
                   'dezessete', 'dezoito', 'dezenove', 'vinte')
numeros_inteiros = tuple(range(0, 21))
while True:
    numero = int(input('Informe um número entre 0 e 20): '))
    if numero in numeros_inteiros:
        print(numeros_extenso[numero])
        break
    else:
        numero = int(input('Informe um número entre 0 e 20): '))
