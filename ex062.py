"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

"""

from cgi import print_arguments


primeiro_termo = int(input('Informe o 1º termo da P.A.: ').strip())
quant_termos = int(input('Informe a quantidade de termos da P.A.: ').strip())
razao = int(input('Informe a razão da P.A.: '))
while quant_termos != 0:
    ultimo_termo = primeiro_termo + (quant_termos - 1) * razao
    print(f'razão: {razao} e último termo: {ultimo_termo}.')
    print('A progressão aritmética resultante será:')
    i = primeiro_termo
    while primeiro_termo <= i <= ultimo_termo:
        print(f'{i}', end=' -> ')
        # termo = primeiro_termo + (i - 1) * razao
        i += razao
    quant_termos = int(input(
        'Informe a quantidade de termos da P.A. (digite 0 caso deseje encerrar o programa): ').strip())
print('ACABOU.', end='')
