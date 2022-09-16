"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

"""


print('Gerador de P.A.')
print('-=' * 10)
primeiro_termo = int(input('Informe o 1º termo da P.A.: ').strip())
razao = int(input('Informe a razão da P.A.: '))
termo = primeiro_termo
cont = 1
total_termos = 0
mais_termos = 10

while mais_termos != 0:
    total_termos = total_termos + mais_termos
    while cont <= total_termos:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termos = int(
        input('Quantos termos você quer imprimir a mais?: ').strip())
print(f'Progessão aritmética finalizada com {total_termos} mostrados.')
print('ACABOU')
