"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:

C, A SACADA DA CASA,
A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

"""
frase = input('Digite uma frase: ').upper().strip().split()
# palavras = frase.split()
junto = ''.join(frase)
ivertida = junto[::-1]
print(f'O inverso de {junto} é {ivertida}.')
if ivertida == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo.')