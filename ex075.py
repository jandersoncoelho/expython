'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

'''
# Armazenar os valores em uma tupla
tupla = (int(input('Digite o 1º valor: ')),
         int(input('Digite o 2º valor: ')),
         int(input('Digite o 3º valor: ')),
         int(input('Digite o 4º valor: ')))

# Contar quantas vezes o valor 9 apareceu na tupla
contador_nove = tupla.count(9)

# Encontrar a posição do primeiro valor 3 na tupla
posicao_tres = tupla.index(3) + 1 if 3 in tupla else None

# Encontrar todos os números pares na tupla
pares = tuple(num for num in tupla if num % 2 == 0)

# Mostrar os resultados
print(f'O valor 9 apareceu {contador_nove} vezes.')

if posicao_tres == None:
    print('O valor 3 não foi encontrado em nenhuma posisão')
else:
    print(f'O primeiro valor 3 foi digitado na posição {posicao_tres}.')

if pares == ():
    print('Você não digitou números pares')
else:
    # print(f'Os números pares digitados foram: {pares}')
    print(f'Os números pares digitados foram: ', end='')

    for par in pares:
        print(par, end=' ')
