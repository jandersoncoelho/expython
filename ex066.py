'''
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

'''
cont = 0
soma_num_informados = 0

while True:
    num_informado = int(
        input('Informe um número inteiro (Informe 999 para encerrar): ').strip())
    if num_informado == 999:
        break
    soma_num_informados += num_informado
    cont += 1
print(f'Foram informados {cont} números e soma deles é {soma_num_informados}.')
