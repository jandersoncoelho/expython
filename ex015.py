"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""
quantidade_km = float(input('Quantos Km o veículo andou? '))
quantidade_dias = int(input('Quantos dias o carro foi alugado? '))
custo_dia = quantidade_dias * 60.00
custo_km = quantidade_km * 0.15
total_a_pagar = custo_dia + custo_km
print('O preço do aluguel do veículo foi R${:.2f}'.format(total_a_pagar))
