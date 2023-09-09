'''
Exercício Python 098:

- Faça um programa que tenha uma função chamada contador().
- Faça com que receba três parâmetros: início, fim e passo.
- Seu programa tem que realizar três contagens através da função criada.
- Primeiro, use a função contador() para realizar a contagem de 1 até 10, de 1 em 1.
- Segundo, de 10 até 0, de 2 em 2.
- Por útimo, peça ao usuário uma contagem personalizada.
- Crie um temporizador dentro da função para mostrar a contagem a cada segundo.


'''
from time import sleep

def escreva(mensagem):
    tamanho_linha = len(mensagem) + 4
    print('~' * tamanho_linha)
    print(mensagem.center(tamanho_linha))
    print('~' * tamanho_linha)


def contador(inicio, fim, passo):
    escreva(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}')
    if (passo > 0):
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(1)
    elif(passo < 0):
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ', flush=True)
            sleep(1)
    else:
        escreva('ERRO! O VALOR DE CONTAGEM TEM QUE SER DIFERENTE DE ZERO!')
        
    print('',end='\n')
    sleep(1)

#Programa principal

contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('Digite um valor para começar a contagem: '))
fim = int(input('Digite um valor para encerrar a contagem: '))
passo = int(input('Digite um valor que será o intervalo da contagem(valores negativos farão contagem regressiva): '))
contador(inicio, fim, passo)
