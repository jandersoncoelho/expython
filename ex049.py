"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.

"""
num = int(input('Informe um número inteiro: ').strip())
print(f'A tabuada de {num} é:')
print('='*12)
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
print('=' * 12)
