"""
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em
graus Celsius e converta para graus Fahrenheit.
Ex.: (0 °C × 9/5) + 32 = 32 °F
"""
temp_celsius = float(input('Informe a temperatura em graus Celsius: '))
temp_fahrenheit = (temp_celsius * 9 / 5) + 32
print('{:.2f}°C convertido é {:.2f}°F'.format(temp_celsius, temp_fahrenheit))
