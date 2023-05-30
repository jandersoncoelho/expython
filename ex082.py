""" 
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

"""
lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = []

while True:
    numero_digitado = int(input('Digite um número: '))
    lista_numeros.append(numero_digitado)

    if numero_digitado % 2 == 0:
        lista_numeros_pares.append(numero_digitado)
    else:
        lista_numeros_impares.append(numero_digitado)

    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Opção inválida. Digite apenas S ou N.')

    if continuar == 'N':
        break
print('-=' * 40)
print(f'A lista com todos os números digitados é: {lista_numeros}')
print(f'A lista com todos os números pares é: {lista_numeros_pares}')
print(f'A lista com todos os números impares é: {lista_numeros_impares}')
print('-=' * 40)
