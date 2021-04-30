"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""
primeiro_termo = int(input('Informe o 1º termo da P.A.: ').strip())
razao = int(input('Informe a razão da P.A.: '))
quant_termos  = int(input('Informe a quantidade de termos da P.A.: ').strip())
ultimo_termo = primeiro_termo + (quant_termos - 1) * razao
print(f'razão: {razao} e último termo: {ultimo_termo}.')
print('A progressão aritmética resultante será:')
i = primeiro_termo
while primeiro_termo <= i <= ultimo_termo:
    print(f'{i}', end=' -> ')
    # termo = primeiro_termo + (i - 1) * razao
    i += razao
print('ACABOU.', end='')
