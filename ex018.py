"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""
from math import sin, cos, tan, radians
angulo = float(input('informe o valor do ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {:.2f}° vale: {:.2f}, o cosseno vale {:.2f} e a tangente vale {:.2f}'.format(angulo, seno, cosseno, tangente))