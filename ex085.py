"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

"""
lista_numeros = [[], []]  # Lista única para armazenar números pares e ímpares

for i in range(1, 8):
    numero = int(input(f"Digite o {i}º valor numérico: "))
    if numero % 2 == 0:
        lista_numeros[0].append(numero)  # Adiciona número par à primeira lista
    else:
        lista_numeros[1].append(numero)  # Adiciona número ímpar à segunda lista

lista_numeros[0].sort()  # Ordena os números pares em ordem crescente
lista_numeros[1].sort()  # Ordena os números ímpares em ordem crescente

# Interpolação de textos para exibir os resultados
print('-=' * 40)
print(f'Os valores pares da lista de números são: {", ".join(str(n) for n in lista_numeros[0])}.')
print(f'Os valores ímpares da lista são: {", ".join(str(n) for n in lista_numeros[1])}.')
