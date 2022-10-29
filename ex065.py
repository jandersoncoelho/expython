'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre:

-> A média entre todos os valores (OK)
-> Qual foi o maior e o menor valores lidos. 
-> O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. (OK)


'''
continuar = 'S'
num_informado = 0
qtd_numeros = 0
maior_numero = 0
menor_numero = 0
soma = 0
while continuar in 'Ss':

    num_informado = int(input('Informe um número inteiro: ').strip())
    qtd_numeros += 1
    soma += num_informado

    if qtd_numeros == 1:
        maior_numero = menor_numero = num_informado
    else:
        if num_informado > maior_numero:
            maior_numero = num_informado
        if num_informado < menor_numero:
            menor_numero = num_informado

    continuar = str(input('Deseja continuar (S/N)? ').strip()[0])

media = soma / qtd_numeros
print(f'Quantidade dos números informados: {qtd_numeros}')
print(f'A média aritmética dos números informados é: {media:,.2f}')
print(f'O maior número informado foi: {maior_numero}')
print(f'O meno número informado foi: {menor_numero}')
