"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

"""
velocidade = float(input('Informe a velocidade do veículo em Km/h: ').strip())
if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print('Sinto muito. Você foi multado!')
    print('O valor da multa será de R${:.2f}.'.format(valor_multa))
else:
    print('Você não ultrapassou o limite de velocidade.')





