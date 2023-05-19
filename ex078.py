'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

'''
lista_numeros = []

# Ler 5 valores numéricos e adicioná-los à lista
for i in range(1, 6):
    valor = int(input(f'Digite o {i}º valor numérico: '))
    lista_numeros.append(valor)

# Encontrar o maior valor e sua posição
maior_valor = max(lista_numeros)
posicoes_maior = [index + 1 for index,
                  num in enumerate(lista_numeros) if num == maior_valor]

# Encontrar o menor valor e sua posição
menor_valor = min(lista_numeros)
posicoes_menor = [index + 1 for index,
                  num in enumerate(lista_numeros) if num == menor_valor]


# Mostrar os resultados
print('=-' * 20)
print('Valores digitados:', lista_numeros)
print(
    f'O maior valor digitado foi {maior_valor} nas posições: {posicoes_maior}')
print(
    f'O menor valor digitado foi {menor_valor} nas posições: {posicoes_menor}')
print('=-' * 20)
