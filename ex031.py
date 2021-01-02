"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas.

"""
distância = float(input('A viagem que você quer fazer tem quantos quilômetros? ').strip())
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('Sua passagem vai custar R${:.2f}.'.format(preço))

# if distância <= 200:
#     print('Sua passagem vai custar R${:.2f}.'.format(distância * 0.50))
# else:
#     print('Sua passagem vai custar R${:.2f}.'.format(distância * 0.45))
