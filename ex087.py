'''

Exercício Python 087: 

Aprimore o exercício anterior, mostrando no final:                                                    

- A soma de todos os valores pares digitados.                                                                                                 
- A soma dos valores da terceira coluna.                                                                                                                
- O maior valor da segunda linha.

'''
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_valores_pares = 0
soma_valores_col3 = 0

# Atribuindo valores à matriz
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input(f'Digite um número na posição ({l}, {c}): '))

        if matriz[l][c] % 2 == 0:
        	soma_valores_pares +=  matriz[l][c]
        	
        if c == 2:
        	soma_valores_col3 += matriz[l][c]
 
# Imprimindo a matriz
print('\nA matriz resultante é:')
print('-' * 40)
for linha in matriz:
    for valor in linha:
        print(f"{valor:>10}", end="")
    print()
print('-' * 40)

print(f'Soma de todos os valores pares digitados: {soma_valores_pares}')
print(f'Soma de todos os valores da terceira coluna: {soma_valores_col3}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')
