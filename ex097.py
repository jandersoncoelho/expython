'''

Exercício Python 097:

- Faça um programa que tenha uma função chamada escreva().
- Ela receberá um texto qualquer como parâmetro.
- Mostre uma mensagem com tamanho adaptável e centralizado.

Ex:

escreva(‘Olá, Mundo!’)

Saída:

~~~~~~~~~ 
Olá, Mundo!
~~~~~~~~~

'''

def escreva(mensagem):
    tamanho_linha = len(mensagem) + 4
    print('~' * tamanho_linha)
    print(mensagem.center(tamanho_linha))
    print('~' * tamanho_linha)

# Programa Principal
texto_mensagem = str(input('Digite uma mensagem: '))
escreva(texto_mensagem)
