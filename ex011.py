'''Faça um programa que leia a largura e a altura de uma parede em metros,
 calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
''''2m²  --- 1 lata
    area --- x latas
    area = 2x
    x = area / 2 '''
altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area_parede = altura * largura
litros_de_tinta = area_parede / 2
print('Você precisa de {:.2f} litros de tinta para pintar {:.2f}m² de parede. '.format(litros_de_tinta, area_parede))
