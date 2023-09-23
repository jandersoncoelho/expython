'''
Exercício Python 100:

- Faça um programa que tenha uma lista chamada números e duas funções.
- Uma chamada sorteia() e a outra somaPar().
- A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

'''

from random import sample

def sorteia(lista_numeros):
    lista_numeros = sample(range(1, 7), 6)
    print(lista_numeros)
    print('=-' * 30)
    soma_par(lista_numeros)
    

def soma_par(lista):
    soma_total = 0
    lista_pares = [numero for numero in lista if numero % 2 == 0]
    print(lista_pares)
    for i in range(len(lista_pares)):
        soma_total += lista_pares[i]
    print('=-' * 30)
    print(f'A soma total dos números pares da lista é: {soma_total}.')

##numeros = sample(range(1, 7), 6)
numeros = list()
sorteia(numeros)
