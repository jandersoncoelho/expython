'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''
continuar = 's'
cont_18 = 0
cont_homens = 0
cont_idade_mulher_menor_20 = 0
while True:

    if continuar in 'Ss':
        sexo = input(
            'Digite o sexo [ M -> Masculino / F -> Feminino]: ').strip()
        while sexo not in 'MmFf':
            sexo = ''
            sexo = input(
                'Digite o sexo [ M -> Masculino / F -> Feminino]: ').strip()

        idade = int(input('Digite a idade da pessoa: ').strip())

        if (idade >= 18):
            cont_18 += 1

        if (sexo in 'Mm'):
            cont_homens += 1

        if ((sexo in 'Ff') and idade < 20):
            cont_idade_mulher_menor_20 += 1

        continuar = str(input('Deseja continuar [S/N]: ').strip())
        while continuar not in 'SsNn':
            continuar = str(input('Deseja continuar [S/N]: ').strip())
    else:
        break
print(f'Foram informadas {cont_18} pessoas com 18 anos ou mais.')
print(f'Foram informados {cont_homens} homens.')
print(
    f'Foram informados {cont_idade_mulher_menor_20} mulheres com menos de 20 anos.')
