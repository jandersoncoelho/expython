"""
Exercício Python 35: Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não
formar um triângulo.

"""
print('=+' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('=+' * 20)

a = float(input('Infome a medida do primeiro segmento: ').strip())
b = float(input('Infome a medida do segundo segmento: ').strip())
c = float(input('Infome a medida do terceiro segmento: ').strip())
if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos {a:.2f} , {b:.2f} e {c:.2f} FORMAM um triângulo.')
else:
    print(f'Os segmentos {a:.2f} , {b:.2f} e {c:.2f} NÃO FORMAM um triângulo.')
