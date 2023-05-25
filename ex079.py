'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''

lista_numeros = []
while True:
    numero_digitado = int(input('Digite um número: '))
    if numero_digitado in lista_numeros:
        print('=' * 40)
        print(f'{"NÚMERO JÁ EXISTE NA LISTA. POR FAVOR DIGITE OUTRO.":^40}')
        print('=' * 40)
    else:
        lista_numeros.append(numero_digitado)

    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Opção inválida. Digite apenas S ou N.')

    if continuar == 'N':
        break
lista_numeros.sort()

print('=' * 40)
print(
    f'A lista de números digitados em ordem crescente é: {lista_numeros}')
