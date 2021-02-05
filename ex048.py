"""
Exercício Python 48: Faça um programa que calcule a
soma entre todos os números que são múltiplos
de três e que se encontram no intervalo
de 1 até 500.

"""
s = 0  # soma
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += contador
        s += c
print(f'A soma de todos os {contador} somados e múltiplos de 3 entre 1 500 é {s}.', end=' ')
