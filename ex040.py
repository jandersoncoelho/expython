"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

"""

nota1 = float(input('Informe a primeira nota: ').strip())
nota2 = float(input('Informe a segunda nota: ').strip())
media = (nota1 + nota2) / 2

print(f'Com notas {nota1:.1f} e {nota2:.1f}, a média do aluno foi {media:.1f}.')
if media >= 7.0:
    print('O aluno foi APROVADO.')
elif 7 > media <= 5:
    print('O aluno foi para RECUPERAÇÃO.')
elif media < 5.0:
    print('O aluno foi REPROVADO.')

