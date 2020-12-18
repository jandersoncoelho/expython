"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida

"""
peso = float(input('Informe o peso (kg): ').strip())
altura = float(input('informe a altura (m): ').strip())
imc = peso / (altura ** 2)
print(f'Seu Índice de Massa Corpórea é: {imc:.2f}')
if imc < 18.50:
    print('Você está abaixo do peso.')
elif 18.50 <= imc < 25.00:
    print('Você está no peso ideal.')
elif 25.00 <= imc < 30.00:
    print('Você está com sobrepeso.')
elif 30.00 <= imc < 40.00:
    print('Você está com obesidade.')
elif imc >= 40.00:
    print('Você está com obesidade mórbida')

