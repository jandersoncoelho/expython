"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou se já passou do
tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date
sexo = int(input('''Informe seu sexo:
[ 1 ] Masculino
[ 2 ] Feminino: 
Opção: '''))
if sexo == 1:

    ano_nascimento = int(input('Informe o ano de nascimento: ').strip())
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    resta = 18 - (ano_atual - ano_nascimento)
    passou = (ano_atual - ano_nascimento) - 18

    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos de idade em {ano_atual}.')
    if idade > 18:
        print(f'Já passou {passou} ano(s) para você se alistar.')
        print(f'Seu alistamento deveria ser em {ano_nascimento + 18}.')
    elif idade < 18:
        print(f'Falta(m) ainda {resta} ano(s) para você se alistar.')
        print(f'Seu alistamento será em {ano_nascimento + 18}.')
    elif idade == 18:
        print(f'Você já tem {idade} ano(s) de idade. Vamos alistar?')
elif sexo == 2:
    print('Você não precisa se alistar.')
else:
    print('Opção inválida!!!')
