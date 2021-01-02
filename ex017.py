"""
Exercício Python 17: Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

"""
from math import hypot

cateto_oposto = float(input('Informe valor do cateto oposto do triângulo: '))
cateto_adjacente = float(input('Informe valor do cateto adjacente do triângulo: '))
# hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa do triâgulo retângulo é de {:.2f}.'.format(hipotenusa))
