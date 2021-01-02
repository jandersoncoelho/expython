"""
Exercício Python 34: Escreva um programa que pergunte o salário de
um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

"""
salario = float(input('Informe o salário do funcionário R$: ').strip())
if salario <= 1250.00:
    # print(f'O salário do funcionário teve um acréssimo 15% e será de R${salario * 1.15:.2f}.')
    print(f'O salário do funcionário teve um acréssimo 15% e será de R${salario + (salario * 15 / 100):.2f}.')
else:
    # print(f'O salário do funcionário teve um acréssimo 10% e será de R${salario * 1.10:.2f}.')
    print(f'O salário do funcionário teve um acréssimo 10% e será de R${salario + (salario * 10 / 100):.2f}.')

