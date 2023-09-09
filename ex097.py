'''

Exercício Python 097:

- Faça um programa que tenha uma função chamada escreva().
- Ela receberá um texto qualquer como parâmetro.
- Mostre uma mensagem com tamanho adaptável e centralizado.
- O programa deve colocar as

Exemplo:

"escreva(‘Olá, Mundo!’)

Saída:

~~~~~~~~~ 
Olá, Mundo!
~~~~~~~~~
"
- O programa deve colocar as linhas sempre maiores que as mensagens
'''

def escreva(mensagem):
    tamanho_linha = len(mensagem) + 4
    print('~' * tamanho_linha)
    print(mensagem.center(tamanho_linha))
    print('~' * tamanho_linha)

# Programa Principal
texto_mensagem = str(input('Digite uma mensagem: '))
escreva(texto_mensagem)
