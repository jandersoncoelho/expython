"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
controle = ''
qtd_homem = 0
qtd_mulher = 0
while controle in 'Ss':
    sexo = input('Informe o sexo da pessoa '
                 'M -> Masculino '
                 'F -> Feminino: ').strip()
    if sexo in 'Mm':
        qtd_homem += 1
    elif sexo in 'Ff':
        qtd_mulher += 1
    else:
        print('SEXO INVÁLIDO!')
    controle = input('Deseja continuar? (S/N): ').strip()
    while controle not in 'SsNn':
        print('OPÇÃO INVÁLIDA! Tente novamente: ')
        controle = input('Deseja continuar? (S/N): ').strip()

print(f'Foram informados {qtd_homem} homens e {qtd_mulher} mulheres.')
