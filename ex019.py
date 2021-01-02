"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

"""
from random import choice

aluno1 = input('informe o nome do primeiro aluno: ')
aluno2 = input('informe o nome do segundo aluno: ')
aluno3 = input('informe o nome do terceiro aluno: ')
aluno4 = input('informe o nome do quarto aluno: ')

turma = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(turma)
print('O aluno sorteado para apagar o quadro é {}.'.format(sorteado))
