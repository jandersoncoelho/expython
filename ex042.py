"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

"""

print('=+' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('=+' * 20)

a = float(input('Infome a medida do primeiro segmento: ').strip())
b = float(input('Infome a medida do segundo segmento: ').strip())
c = float(input('Infome a medida do terceiro segmento: ').strip())
if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos {a:.2f} , {b:.2f} e {c:.2f} FORMAM um triângulo. ', end='')
    if a == b == c:
        print('E também é EQUILÁTERO.')
    elif a != b != c != a:
        print('E também é ESCALENO.')
    else:
        print('E também é ISÓSCELES.')
else:
    print(f'Os segmentos {a:.2f} , {b:.2f} e {c:.2f} NÃO FORMAM um triângulo.')
