def fatorial(n):
    fat = 1
    for c in range(1, n + 1):
        fat *= c
    return fat

numero = int(input("Digite um número: "))
f = fatorial(numero)
print(f'O fatorial de {numero} é {f}')
