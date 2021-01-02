"""
Exercício Python 13: Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com 15% de aumento.

"""
salario_anterior = float(input('Informe o salário do funcionário: R$'))
salario_reajustado = salario_anterior + (salario_anterior * 15/100)
print('O salário do funcionário com reajuste de 15% passou de R${:.2f} para R${:.2f}.'.format(salario_anterior, salario_reajustado))