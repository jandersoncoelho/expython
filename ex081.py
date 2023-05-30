'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.

'''

lista_numeros = []
while True:
    numero_digitado = int(input('Digite um número: '))
    lista_numeros.append(numero_digitado)

    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Opção inválida. Digite apenas S ou N.')

    if continuar == 'N':
        break

quant_num_digitados = len(lista_numeros)
lista_numeros.sort(reverse=True)
tem_cinco = 5 in lista_numeros

print('-=' * 40)
print(f'Esta lista tem {quant_num_digitados} elementos.')
print(f'Esta lista na forma decrescente fica {lista_numeros}.')
print(f'O valor 5 {"está" if tem_cinco else "não está"} na lista.')
