'''

Exercício Python 096:

 - Faça um programa que tenha uma função chamada área().

 - Essa função vai dimensões de um terreno retangular.

 - A área de um terreno retangular é a multiplicação da lagura vezes o comprimento.

 - Mostre a área do terreno.

'''

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área do terreno é {area_terreno:5.2f}m².')


# Programa Principal
largura = float(input('Digite a largura do terreno (em metros): '))
comprimento = float(input('Digite o comprimento do terreno (em metros): '))

area(largura, comprimento)
