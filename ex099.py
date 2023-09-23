'''
Exercício Python 099:

- Faça um programa que tenha uma função chamada maior()

- Ela receberá vários parâmetros com valores inteiros.

- Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''
def escreva(mensagem):
    tamanho_linha = len(mensagem) + 4
    print('~' * tamanho_linha)
    print(mensagem.center(tamanho_linha))
    print('~' * tamanho_linha)

def maior(*valores):
    if len(valores) == 0:
        escreva('Nenhum valor foi informado.')
    else:
        maior_valor = max(valores)
        escreva(f'Recebi os valores {valores}, que ao todo são {len(valores)} números e o maior deles é {maior_valor}.')
        
# Exemplo de uso da função
maior(5, 8, 2, 12, 7)
maior(5, 8, 2, 12, 7, 0, 100)
maior(0)
maior()
