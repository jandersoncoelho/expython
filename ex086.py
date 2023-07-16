"""
Exercício Python 086: 

- Crie um programa que declare uma matriz de dimensão 3×3.
- Preencha com valores lidos pelo teclado. 
- No final, mostre a matriz na tela, com a formatação correta.

"""


matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Atribuindo valores à matriz
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input(f'Digite um número na posição ({l}, {c}): '))

# Imprimindo a matriz
print('\nA matriz resultante é:')
print('-' * 40)
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end="")
    print()
print('-' * 40)
