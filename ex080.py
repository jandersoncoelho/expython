
'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''
lista_numeros = []

for _ in range(5):
    numero_digitado = int(input('Digite um número: '))

    if not lista_numeros:
        lista_numeros.append(numero_digitado)
    else:
        for i, num in enumerate(lista_numeros):
            if numero_digitado < num:
                lista_numeros.insert(i, numero_digitado)
                break
        else:
            lista_numeros.append(numero_digitado)

print('A lista de números digitados em ordem crescente é:', lista_numeros)
