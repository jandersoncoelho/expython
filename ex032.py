"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual:  '.strip()))
if ano == 0:
    ano = date.today().year
if (ano % 400 == 0) or ((ano % 100 != 0) and (ano % 4 == 0)):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))
